# -*- coding: utf-8 -*-
import urllib
from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from forms import PaymentForm
from vnpay import vnpay
from django.conf import settings
from booking.models import BookingInfomation
from booking import api
from booking import booking_handle
from core.decorator import *
from core.metiz_cipher import MetizAESCipher
from core import metiz_util
import json
from django.core.urlresolvers import reverse

# def cancel_seats(seats_choice, id_server):
#     for seat in seats_choice:
#         api.call_api_cancel_seat(seat, id_server=id_server)


@check_user_booking_exist
def payment(request):
    if request.method == 'POST':
        # Process input data and build url payment
        form = PaymentForm(request.POST)
        barcode = request.POST.get("barcode", None)
        seats_choice = request.POST.get("seats_choice", None)
        working_id = request.POST.get("working_id", None)
        id_server = request.POST.get("id_server", 1)
        movie_poster = request.POST.get("movie_poster", "")


        print "request.POST", request.POST

        # Verify Session Booking Timeout before redirect to vnpayment
        movies_session = request.session.get("movies", "")
        print "@@@@@ movies_session ",movies_session
        # if not movies_session or (movies_session and working_id not in movies_session):
        #     return redirect(reverse('time-out') + '?page=payment')

        total_payment_store = movies_session[working_id]["total_money"]
        if form.is_valid():
            # decrypt amount value 
            try:
                amount_encrypt = form.cleaned_data['amount']
                cipher = MetizAESCipher()    
                amount = cipher.decrypt(amount_encrypt)
                
                # Verify Money Booking
                if int(amount) < int(total_payment_store):
                    print "total_payment_store ",total_payment_store
                    print "amount ",amount
                    return redirect("invalid-booking")

            except Exception, e:
                "Error Decrypt money ",e
                return render(request, "websites/vnpay_payment/payment.html",
                      {"form": form,
                       "total_payment": "",
                       "order_desc": request.POST["order_desc"] if 'order_desc' in request.POST["order_desc"] else None})

            order_type = form.cleaned_data['order_type']
            order_id = form.cleaned_data['order_id']
            

            order_desc = form.cleaned_data['order_desc']
            bank_code = form.cleaned_data['bank_code']
            language = form.cleaned_data['language']
            ipaddr = get_client_ip(request)
            # Build URL Payment
            vnp = vnpay()
            vnp.requestData['vnp_Version'] = '2.0.0'
            vnp.requestData['vnp_Command'] = 'pay'
            vnp.requestData['vnp_TmnCode'] = settings.VNPAY_TMN_CODE
            vnp.requestData['vnp_Amount'] = int(amount) * 100
            vnp.requestData['vnp_CurrCode'] = 'VND'
            vnp.requestData['vnp_TxnRef'] = order_id
            vnp.requestData['vnp_OrderInfo'] = order_desc
            vnp.requestData['vnp_OrderType'] = order_type
            # Check language, default: vn
            if language and language != '':
                vnp.requestData['vnp_Locale'] = language
            else:
                vnp.requestData['vnp_Locale'] = 'vn'
                # Check bank_code, if bank_code is empty, customer will be
                # selected bank on VNPAY
            if bank_code and bank_code != "":
                vnp.requestData['vnp_BankCode'] = bank_code

            vnp.requestData['vnp_CreateDate'] = datetime.now(
            ).strftime('%Y%m%d%H%M%S')  # 20150410063022
            vnp.requestData['vnp_IpAddr'] = ipaddr
            vnp.requestData['vnp_ReturnUrl'] = settings.VNPAY_RETURN_URL
            vnpay_payment_url = vnp.get_payment_url(
                settings.VNPAY_PAYMENT_URL, settings.VNPAY_HASH_SECRET_KEY)

            # Remove session and store order in database and verify order id
            # unsuccessfull, clear seats

            if movies_session and working_id in movies_session:
                del request.session['movies'][working_id]

            # Store order infomation with status is pendding
            booking_order = BookingInfomation(order_id=order_id, order_desc=order_desc, amount=amount, phone=request.session.get("phone", ""),
                                              email=request.session.get("email", ""), seats=seats_choice, barcode=barcode,
                                              id_server=id_server, order_status="pendding", poster=movie_poster, gate_payment="VNPay")

            if not request.user.is_anonymous():
                booking_order.user = request.user
            booking_order.save()

            print(vnpay_payment_url)
            if request.is_ajax():
                # Show VNPAY Popup
                result = JsonResponse(
                    {'code': '00', 'Message': 'Init Success', 'data': vnpay_payment_url})
                return result
            else:
                # Redirect to VNPAY
                return redirect(vnpay_payment_url)
        else:
            print("Form input not validate %s" % form.errors)
            return render(request, "websites/vnpay_payment/payment.html",
                          {"form": form,
                           "total_payment": request.POST["amount"] if 'amount' in request.POST["amount"] else None,
                           "order_desc": request.POST["order_desc"] if 'order_desc' in request.POST["order_desc"] else None})
    # else:
    #     data_encrypt = request.GET.get('data', 0)
        
    #     # Decrypt data payment form contain : total payment , seats choice ..etc
    #     cipher = MetizAESCipher()    
    #     decrypted = cipher.decrypt(data_encrypt)
    #     data_json = json.loads(decrypted)
        
    #     total_payment = data_json['totalPayment'] if 'totalPayment' in data_json else 0
    #     seats = metiz_util.remove_uni(str(data_json['seats'])) if 'seats' in data_json else ""
    #     working_id = data_json['working_id'] if 'working_id' in data_json else ""
    #     barcode = data_json['barcode'] if 'barcode' in data_json else ""
    #     # Handle list seats to string and remove unicode
    #     seat_array = ','.join(data_json['seats_choice']) 
    #     seats_choice = metiz_util.remove_uni(seat_array) if 'seats_choice' in data_json else ""
        
    #     id_server = data_json['id_server'] if 'id_server' in data_json else 1
    #     id_showtime = data_json['id_showtime'] if 'id_showtime' in data_json else ""
    #     movie_api_id = data_json['movie_api_id'] if 'movie_api_id' in data_json else ""
    #     id_movie_name = data_json['id_movie_name'] if 'id_movie_name' in data_json else ""
    #     id_movie_time = data_json['id_movie_time'] if 'id_movie_time' in data_json else ""
    #     id_movie_date_active = data_json['id_movie_date_active'] if 'id_movie_date_active' in data_json else ""

    #     return render(request, "websites/vnpay_payment/payment.html",
    #                   {"title": "Thanh toán", "total_payment": total_payment, "seats": seats,
    #                    "working_id": working_id, "barcode": barcode, "seats_choice": seats_choice, "id_server": id_server, "id_showtime": id_showtime,
    #                    "id_movie_name": id_movie_name, "id_movie_time": id_movie_time, "id_movie_date_active": id_movie_date_active,
    #                    "movie_api_id": movie_api_id})


def payment_ipn(request):
    """ Process Status Payment """
    inputData = request.GET
    if inputData:
        vnp = vnpay()
        vnp.responseData = inputData.dict()
        order_id = inputData['vnp_TxnRef']
        amount = inputData['vnp_Amount']
        order_desc = inputData['vnp_OrderInfo']
        vnp_TransactionNo = inputData['vnp_TransactionNo']
        vnp_ResponseCode = inputData['vnp_ResponseCode']
        vnp_TmnCode = inputData['vnp_TmnCode']
        vnp_PayDate = inputData['vnp_PayDate']
        vnp_BankCode = inputData['vnp_BankCode']
        vnp_CardType = inputData['vnp_CardType']
        if vnp.validate_response(settings.VNPAY_HASH_SECRET_KEY):
            # Check & Update Order Status in your Database
            try:
                """ 
                    get booking order verify with vnpayment 
                    step 1: get booking order by id, 
                            return code 00 if process successfully. 
                            return code 01 if order_id not found. 
                            return code 02 if order have been process before.
                            return code 99 if process booking movie error.
                    step 2: Call Api Confirm Booking and send sms or email if success
                    Step 3: Handle payment process error
                """
                booking_order = BookingInfomation.objects.get(
                    order_id=order_id)

                # Verify Order_id proccess update before
                if booking_order.order_status == 'done':
                    return JsonResponse({'RspCode': '02', 'Message': 'Order Already Update'})

                if vnp_ResponseCode == '00':
                    # handle confirm booking and send sms , email
                    booking_handle.process_confirm_booking(request, booking_order, amount)
                    
                    # Return VNPAY: Merchant update success
                    result = JsonResponse(
                        {'RspCode': '00', 'Message': 'Confirm Success'})
                else:
                    print('Payment Error. Processing Payment Error')
                    # Payment Error: cancel seats chooice and return for
                    # vnpayment
                    # if booking_order.seats:
                    #     cancel_seats(booking_order.seats.split(
                    #         ","), booking_order.id_server)

                    booking_order.order_status = 'payment_error'
                    booking_order.save()

                    result = JsonResponse(
                        {'RspCode': '00', 'Message': 'Confirm Error'})

            except BookingInfomation.DoesNotExist, e:
                print "Error BookingInfomation DoesNotExist : %s" % e
                return JsonResponse(
                    {'RspCode': '01', 'Message': 'Order_id Not Found'})

        else:
            # Invalid Signature
            result = JsonResponse(
                {'RspCode': '97', 'Message': 'Invalid Signature'})
    else:
        result = JsonResponse({'RspCode': '99', 'Message': 'Invalid request'})

    return result


def payment_return(request):
    inputData = request.GET
    if inputData:
        vnp = vnpay()
        vnp.responseData = inputData.dict()
        order_id = inputData['vnp_TxnRef']
        amount = int(inputData['vnp_Amount']) / 100
        order_desc = inputData['vnp_OrderInfo']
        vnp_TransactionNo = inputData['vnp_TransactionNo']
        vnp_ResponseCode = inputData['vnp_ResponseCode']
        vnp_TmnCode = inputData['vnp_TmnCode']
        vnp_PayDate = inputData['vnp_PayDate']
        vnp_BankCode = inputData['vnp_BankCode']
        vnp_CardType = inputData['vnp_CardType']
        barcode = None
        try:
            booking_order = BookingInfomation.objects.get(order_id=order_id)
            barcode = booking_order.barcode
        except BookingInfomation.DoesNotExist, e:
            print "Error BookingInfomation DoesNotExist : %s" % e
            pass

        if vnp.validate_response(settings.VNPAY_HASH_SECRET_KEY):
            if vnp_ResponseCode == "00":
                # Success Send SMS or email infomation order for user
                return render(request, "websites/vnpay_payment/payment_return.html", {"title": "Kết quả thanh toán",
                                                                                      "result": "Thành công", "order_id": order_id,
                                                                                      "amount": amount,
                                                                                      "order_desc": order_desc,
                                                                                      "vnp_TransactionNo": vnp_TransactionNo,
                                                                                      "vnp_ResponseCode": vnp_ResponseCode,
                                                                                      "barcode": barcode})
            else:

                return render(request, "websites/vnpay_payment/payment_return.html", {"title": "Kết quả thanh toán",
                                                                                      "result": "Lỗi", "order_id": order_id,
                                                                                      "amount": amount,
                                                                                      "order_desc": order_desc,
                                                                                      "vnp_TransactionNo": vnp_TransactionNo,
                                                                                      "vnp_ResponseCode": vnp_ResponseCode,
                                                                                      "barcode": barcode})
        else:
            return render(request, "websites/vnpay_payment/payment_return.html",
                          {"title": "Kết quả thanh toán", "result": "Lỗi", "order_id": order_id, "amount": amount,
                           "order_desc": order_desc, "vnp_TransactionNo": vnp_TransactionNo,
                           "vnp_ResponseCode": vnp_ResponseCode, "msg": "Sai checksum", "barcode": barcode})
    else:
        return render(request, "websites/vnpay_payment/payment_return.html", {"title": "Kết quả thanh toán", "result": ""})


def query(request):
    if request.method == 'GET':
        return render(request, "websites/vnpay_payment/query.html", {"title": "Kiểm tra kết quả giao dịch"})
    else:
        # Add paramter
        vnp = vnpay()
        vnp.requestData = {}
        vnp.requestData['vnp_Command'] = 'querydr'
        vnp.requestData['vnp_Version'] = '2.0.0'
        vnp.requestData['vnp_TmnCode'] = settings.VNPAY_TMN_CODE
        vnp.requestData['vnp_TxnRef'] = request.POST['order_id']
        vnp.requestData[
            'vnp_OrderInfo'] = 'Kiem tra ket qua GD OrderId:' + request.POST['order_id']
        vnp.requestData['vnp_TransDate'] = request.POST[
            'trans_date']  # 20150410063022
        vnp.requestData['vnp_CreateDate'] = datetime.now(
        ).strftime('%Y%m%d%H%M%S')  # 20150410063022
        vnp.requestData['vnp_IpAddr'] = get_client_ip(request)
        requestUrl = vnp.get_payment_url(
            settings.VNPAY_API_URL, settings.VNPAY_HASH_SECRET_KEY)
        responseData = urllib.urlopen(requestUrl).read().decode()
        print('RequestURL:' + requestUrl)
        print('VNPAY Response:' + responseData)
        data = responseData.split('&')
        for x in data:
            tmp = x.split('=')
            if len(tmp) == 2:
                vnp.responseData[tmp[0]] = urllib.unquote(
                    tmp[1]).replace('+', ' ')

        print('Validate data from VNPAY:' +
              str(vnp.validate_response(settings.VNPAY_HASH_SECRET_KEY)))
        return render(request, "websites/vnpay_payment/query.html", {"title": "Kiểm tra kết quả giao dịch", "data": vnp.responseData})


def refund(request):
    return render(request, "websites/vnpay_payment/refund.html", {"title": "Gửi yêu cầu hoàn tiền"})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
