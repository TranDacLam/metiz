# -*- coding: utf-8 -*-
import urllib
from datetime import datetime

from django.core.serializers import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.sites.models import Site
from forms import PaymentForm
from vnpay import vnpay
from django.conf import settings
from booking.models import BookingInfomation
from booking import api
from registration import metiz_email
from Crypto.Cipher import AES
import ast
import requests
import random
import base64
from core.models import AdminInfo


def data_encrypt_cbc(data):
    """ encrypt content data with padding """
    # padding = block_size - (len(data) % block_size)
    # padding = 16 - (len(data) % 16)
    # str_with_padding = data + chr(padding)*padding
    block_size = 16
    padding = block_size - (len(data) % block_size)
    data += chr(padding) * padding

    AES.key_size = 128

    crypt_object = AES.new(key=settings.SMS_KEY,
                           mode=AES.MODE_CBC, IV=settings.SMS_KEY_IV)

    encrypted_text = crypt_object.encrypt(data)

    return base64.b64encode(encrypted_text)


def send_sms(phone, content):
    try:
        if str(phone).startswith("84"):
            phone_number = str(phone)
        elif str(phone).startswith("0"):
            phone_number = "84" + str(phone)[1:]
        else:
            phone_number = "84" + str(phone)
        content_sms = content
        id_sms = random.randint(0, 999)
        time_send = timezone.localtime(timezone.now()).strftime("%Y%m%d%H%M%S")
        brand = settings.SMS_BRAND
        xml = "<content><ReceiverPhone>%s</ReceiverPhone><Message>%s</Message><RequestID>%s</RequestID><BrandName>%s</BrandName><Senttime>%s</Senttime></content>" % (
            str(phone_number), str(content_sms), str(id_sms), brand, str(time_send))

        xml_encode = data_encrypt_cbc(xml.replace("\r\n", ""))  # mã hóa
        user_ctnet = data_encrypt_cbc(settings.SMS_USER)
        pass_ctnet = data_encrypt_cbc(settings.SMS_PASSWORD)

        soap_request = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n"
        soap_request += "<soap:Envelope xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">\n"
        soap_request += "<soap:Body>\n"
        soap_request += "<sendsms xmlns=\"http://tempuri.org/\">\n"
        soap_request += "<user>%s</user>\n" % user_ctnet
        soap_request += "<pass>%s</pass>\n" % pass_ctnet
        soap_request += "<xml>%s</xml>\n" % xml_encode
        soap_request += "</sendsms>\n"
        soap_request += "</soap:Body>\n"
        soap_request += "</soap:Envelope>"

        headers = {
            "Content-type": "text/xml;charset=\"utf-8\"",
            "Accept": "text/xml",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "SOAPAction": "\"http://tempuri.org/sendsms\"",
            "Content-length": "%s" % len(soap_request),
        }
        response = requests.post(
            settings.SMS_URL, data=soap_request, headers=headers)
        print "SOAP  Ressponse ", response.content
        return response.content

    except Exception, e:
        print "Error send_sms : %s" % e
        pass
        return None

def send_mail_booking(is_secure, email, full_name, barcode, content):
    try:
        message_html = "websites/booking/email/booking_notification.html"
        subject = _("[Metiz] Booking Movie Tickets Successful !")

        protocol = 'http'
        if is_secure:
            protocol = 'https'
        logo_url = '/static/assets/websites/images/logo_bottom.png'
        data_binding = {
            "protocol": protocol,
            'full_name': full_name,
            'URL_LOGO': logo_url,
            'barcode': barcode,
            'content': content,
            'site': str(Site.objects.get_current())
        }
        # Send email booking success
        metiz_email.send_mail(subject, None, message_html, settings.DEFAULT_FROM_EMAIL, [
                              email], data_binding)
    except Exception, e:
        print "Error send_mail_booking : ", e

def send_mail_booking_error(is_secure, email, barcode, content):
    try:
        message_html = "websites/booking/email/booking_error.html"
        subject = _("[Metiz] Booking Movie Tickets Transaction Error !")

        protocol = 'http'
        if is_secure:
            protocol = 'https'
        logo_url = '/static/assets/websites/images/logo_bottom.png'
        data_binding = {
            "protocol": protocol,
            'URL_LOGO': logo_url,
            'barcode': barcode,
            'content': content,
            'site': str(Site.objects.get_current())
        }
        # Send email transaction booking moive order error
        metiz_email.send_mail(subject, None, message_html, settings.DEFAULT_FROM_EMAIL, [
                              email], data_binding)
    except Exception, e:
        print "Error send_mail_booking : ", e


def cancel_seats(seats_choice, id_server):
    for seat in seats_choice:
        api.call_api_cancel_seat(seat, id_server=id_server)


def payment(request):
    if request.method == 'POST':
        # Process input data and build url payment
        form = PaymentForm(request.POST)
        barcode = request.POST.get("barcode", None)
        seats_choice = request.POST.get("seats_choice", None)
        working_id = request.POST.get("working_id", None)
        id_server = request.POST.get("id_server", 1)

        # Verify Session Booking Timeout before redirect to vnpayment
        movies_session = request.session.get("movies", "")
        if not movies_session or (movies_session and working_id not in movies_session):
            return redirect("time-out-booking")

        if form.is_valid():
            order_type = form.cleaned_data['order_type']
            order_id = form.cleaned_data['order_id']
            amount = form.cleaned_data['amount']
            order_desc = form.cleaned_data['order_desc']
            bank_code = form.cleaned_data['bank_code']
            language = form.cleaned_data['language']
            ipaddr = get_client_ip(request)
            # Build URL Payment
            vnp = vnpay()
            vnp.requestData['vnp_Version'] = '2.0.0'
            vnp.requestData['vnp_Command'] = 'pay'
            vnp.requestData['vnp_TmnCode'] = settings.VNPAY_TMN_CODE
            vnp.requestData['vnp_Amount'] = amount * 100
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
                                              id_server=id_server, order_status="pendding")

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
    else:
        total_payment = request.GET.get('totalPayment', 0)
        seats = request.GET.get('seats', "")
        working_id = request.GET.get('working_id', "")
        barcode = request.GET.get('barcode', "")
        seats_choice = request.GET.get('seats_choice', "")
        id_server = request.GET.get('id_server', 1)
        id_showtime = request.GET.get('id_showtime', "")
        movie_api_id = request.GET.get('movie_api_id', "")
        id_movie_name = request.GET.get('id_movie_name', "")
        id_movie_time = request.GET.get('id_movie_time', "")
        id_movie_date_active = request.GET.get('id_movie_date_active', "")

        return render(request, "websites/vnpay_payment/payment.html",
                      {"title": "Thanh toán", "total_payment": total_payment, "seats": seats,
                       "working_id": working_id, "barcode": barcode, "seats_choice": seats_choice, "id_server": id_server, "id_showtime": id_showtime,
                       "id_movie_name": id_movie_name, "id_movie_time": id_movie_time, "id_movie_date_active": id_movie_date_active,
                       "movie_api_id": movie_api_id})


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
                    print('Payment Success. Processing Booking Confirm')
                    id_server = booking_order.id_server if booking_order.id_server else 1
                    # Payment Success update order status and  call api confirm
                    # booking order
                    result_confirm = api.call_api_booking_confirm(
                        booking_order.barcode, id_server)

                    # Handle Confirm Booking Error
                    # ReCall confirm booking three times when booking confirm error
                    recall = 1
                    error_comfirm = True
                    status_confirm = result_confirm["SUCCESS"]
                    
                    while status_confirm == 'false' and recall <= 3:
                        # recall api confirm booking
                        result_confirm = api.call_api_booking_confirm(
                             booking_order.barcode, id_server)
                        # update new status of api
                        status_confirm = result_confirm["SUCCESS"]
                        error_comfirm = False if status_confirm == 'true' else True
                        recall +=1
                            
                    if error_comfirm:
                        # update number retry ipn
                        booking_order.order_status = 'confirm_error'
                        booking_order.desc_transaction = "Payment success but confirm booking error"
                        booking_order.save()
                        
                        
                        # Payment Error: cancel seats chooice and return for
                        # vnpayment
                        if booking_order.seats:
                            cancel_seats(booking_order.seats.split(
                                ","), booking_order.id_server)

                        # Get information admin metiz cinema
                        email_admin_cinema = settings.SYSTEM_ADMIN_CINEMA_EMAIL
                        phone_admin = settings.SYSTEM_ADMIN_CINEMA_PHONE

                        admin_info = AdminInfo.objects.all()
                        if admin_info:
                            email_admin_cinema = admin_info[0].email
                            phone_admin = admin_info[0].phone

                        # send sms for client about transaction booking movie error.
                        error_sms = """Dat ve khong thanh cong tai Metiz Cinema .Ma dat ve: %s, vui long lien he: %s, neu ban van chua duoc hoan tien""" %(booking_order.barcode, phone_admin)
                        # Send SMS notification for user transaction error
                        send_sms(booking_order.phone, error_sms)

                        content_error = """Lỗi: Đã trừ tiền của khách hàng nhưng không thể xuất vé phim. 
                                            Vui Lòng kiểm tra hoá đơn : %s .Để hoàn tiền hoặc xử lý vé cho khách hàng. 
                                            Thông tin khách hàng. Phone: 0%s, email: %s"""%(booking_order.order_id, booking_order.phone, booking_order.email)
                        # Send email notification for admin transaction error
                        print "### email_admin_cinema ",email_admin_cinema
                        if email_admin_cinema:
                            send_mail_booking_error(request.is_secure(), email_admin_cinema, booking_order.barcode, content_error)
                            
                        return JsonResponse({'RspCode': '02', 'Message': 'Process Confirm Booking Movie Error'})

                    # Handle Confirm Booking Success and send sms or email
                    booking_order.order_status = "done"
                    booking_order.save()

                    content_sms = """Ban da dat ve thanh cong tai Metiz Cinema. Ma dat ve: %s, """ % booking_order.barcode
                    content_sms += str(booking_order.order_desc.replace("\r\n", ""))
                    # Send SMS for user
                    send_sms(booking_order.phone, content_sms)

                    # Send Email
                    if booking_order.email:
                        send_mail_booking(request.is_secure(), booking_order.email, request.session.get(
                            "full_name", ""), booking_order.barcode, booking_order.order_desc)

                    # Return VNPAY: Merchant update success
                    result = JsonResponse(
                        {'RspCode': '00', 'Message': 'Confirm Success'})
                else:
                    print('Payment Error. Processing Payment Error')
                    # Payment Error: cancel seats chooice and return for
                    # vnpayment
                    if booking_order.seats:
                        cancel_seats(booking_order.seats.split(
                            ","), booking_order.id_server)

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
