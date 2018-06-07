# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.conf import settings
from decimal import Decimal, ROUND_HALF_UP
from django.http import Http404, JsonResponse, HttpResponseNotFound, HttpResponse
import urllib2
import json
import metiz_otp
from core.metiz_cipher import MetizAESCipher
from core import metiz_util, metiz_sms
from forms import MetizOTPForm
from booking import api, booking_handle
from booking.models import BookingInfomation


"""
    Author : TienDang
    Description: Function handle protected hacking change infomation booking
"""
def invalid_payment(request):
    try:
        """ Action render page notification invalid money """
        return render(request, 'websites/metiz_payment/invalid_method.html')
    except Exception, e:
        print "Error invalid_payment : ", e
        raise Exception(
            "ERROR : Internal Server Error .Please contact administrator.")

"""
    Author : TienDang
    Description: Function handle render page payment methods for action GET , and process redirect to payment gate for action POST
"""
def metiz_payment_methods(request):
    data_encrypt = request.GET.get('data', 0)
    if not data_encrypt:
        raise Http404()

    # Decrypt data payment form contain : total payment , seats choice ..etc
    cipher = MetizAESCipher()    
    decrypted = cipher.decrypt(data_encrypt)
    data_json = json.loads(decrypted)
    
    # Check data and set default if empty and remove special unicode for seats
    total_payment = data_json['totalPayment'] if 'totalPayment' in data_json else 0
    id_server = data_json['id_server'] if 'id_server' in data_json else 1
    seat_count = len(data_json['seats'])
    seats_name = ','.join(data_json['seats']) 
    seats = metiz_util.remove_uni(seats_name) if 'seats' in data_json else ""
    seat_array = ','.join(data_json['seats_choice']) 
    seats_choice = metiz_util.remove_uni(seat_array) if 'seats_choice' in data_json else ""
    
    # append new data for data_json
    data_json["seats"] = seats
    data_json["seats_choice"] = seats_choice
    data_json["total_payment"] = total_payment
    data_json["id_server"] = id_server
    data_json["seat_count"] = seat_count
    

    
    if request.method == "GET":
        return render(request, "websites/metiz_payment/payment_method.html",{"data_json":data_json})

    elif request.method == "POST":
        # Verify Payment Gate for protected hacking
        payment_gate = request.POST.get("payment-gate")
        if payment_gate not in ['Metiz_Payment_Card', 'Helio_Payment_Card', 'VNPay'] or not payment_gate:
            return redirect("invalid-payment")
        
        data_json["payment_gate"] = payment_gate

        working_id = data_json['working_id']

        # Get total money of ticket into session
        movies_session = request.session.get("movies", "")
        try:
            # Verify Session Booking Timeout before process otp
            if not movies_session or (movies_session and working_id not in movies_session):
                return redirect("time-out-booking")

            total_payment_store = movies_session[working_id]["total_money"]
        except (KeyError, TypeError), e:
            return redirect("time-out-booking")
                
        # Verify Money Booking
        if int(data_json["total_payment"]) != int(total_payment_store):
            print "total_payment_store ",total_payment_store
            print "amount ",total_payment
            return redirect("invalid-booking")


        if payment_gate == "VNPay":
            return render(request, "websites/vnpay_payment/payment.html",data_json)

        data_json['order_desc'] = """
                                Phim: %s, Suat chieu: %s, Ngay: %s, Ghe: %s, Rap: Metiz Cinema.
                                """%(data_json["id_movie_name"], data_json["id_movie_time"], data_json["id_movie_date_active"], data_json["seats"])
        return render(request, "websites/metiz_payment/metiz_payment.html", data_json)

def check_amount_and_timeout(movies_session, working_id, result):
    try:
        # Verify Session Booking Timeout before process otp
        print "movies_session ",movies_session
        if not movies_session or (movies_session and working_id not in movies_session):
            print "### DEBUG 1"
            return redirect("time-out-booking")

        total_payment_store = movies_session[working_id]["total_money"]
        
        amount_ticket = total_payment_store
        amount_fb = 0
        amount = amount_ticket + amount_fb
        result['amount_ticket'] = amount_ticket
        result['amount_fb'] = amount_fb
        result['total_payment_store'] = total_payment_store
        # Verify Money Booking
        if int(amount) < int(total_payment_store):
            print "### MONEY "
            return redirect("invalid-booking")

        return True
    except (KeyError, TypeError), e:
        print "### DEBUG 2"
        return redirect("time-out-booking")



def generate_otp(request):
    """ 
        Action Generate OTP for User using Metiz or Helio Payment Card 
        Step 1 : Verify Card Error is : 00 - Payment Success, 01 - Not enough money, 02 - Card is suspended, 03 - Card is replaced, 04 - Card is not exist, 05 - Other Error
        Step 2 : Generate OTP
        Step 3 : Send OTP via SMS to Phone register into payment card
        
    """
    try:
        print "request.POST ",request.POST
        working_id = request.POST.get("working_id", None)
        movies_session = request.session.get("movies", "")
        # set output variable for funtion check working_id
        
        amount = 0
        money_store_dict = {"amount_ticket": 0, "amount_fb": 0} 

        result_check = check_amount_and_timeout(movies_session, working_id, money_store_dict)

        print "#### AMOUNT ",money_store_dict
        if not money_store_dict["amount_ticket"]:
            return result_check

        # Append data for form using detect request hacking
        form_otp = MetizOTPForm(request.POST)
        # init data cache for page
        data_payment = request.POST.dict()
        print "### OTP FORM ",form_otp.is_valid()
        if form_otp.is_valid():
            card_barcode = form_otp.cleaned_data["card_barcode"]

            url_verify_card = settings.HELIO_API_DMZ_URL + "/api/helio/card/payment/"
            # new Request Request
            data = {
                "card_barcode": card_barcode,
                "cashier_id": "0",
                "pos_id": "0",
                "bill_number": form_otp.cleaned_data["order_id"],
                "amount_ticket": money_store_dict["amount_ticket"],
                "amount_fb": money_store_dict["amount_fb"],
                "payment_value": "cash_balance",
                "system_name": "metiz_online",
                "is_verify": True
             }
            
            request_verify = urllib2.Request(url_verify_card, data=json.dumps(data), headers={
                                      'Content-Type': 'application/json', 'Authorization': 'Bearer %s' % settings.DMZ_API_TOKEN})

            # Call api and response data
            try:
                resp = urllib2.urlopen(request_verify)
                result_verify = json.loads(resp.read())
                phone_number = result_verify["phone_number"]

                # Begin generate otp
                code_otp = metiz_otp.opt_user()
                if code_otp["code_otp"] == "000000":
                    data_payment["card_error"] = "System API Error. Please Contact Administrator."
                    return render(request, "websites/metiz_payment/metiz_payment.html", data_payment)

                request.session["movies"][working_id]['secret_key_otp'] = code_otp["secret_key_otp"]
                print "### OTP FOR USER ",code_otp
                print "cap nhat session ",request.session["movies"][working_id]

                # Begin send SMS OTP for User
                sms_otp = """Quy khach dang thuc hien giao dich mua ve tai Metiz Cinema voi so tien la: %s. Ma xac nhan : %s""" %(money_store_dict["amount_ticket"], str(code_otp["code_otp"]))
                metiz_sms.send_sms(phone_number, sms_otp)

                # hidden phone suggest for user
                phone_hide = phone_number[:3] + 'xxxx' + phone_number[-3:]
                data_payment['phone_hide'] = phone_hide
                return render(request, "websites/metiz_payment/payment_verify.html", data_payment)
            except urllib2.HTTPError, e:
                
                result_error = json.loads(e.read())
                print "EXEPTION VERIFY CARD ", result_error
                data_payment["card_error"] = result_error["message"]
                print "data_payment ",data_payment
                return render(request, "websites/metiz_payment/metiz_payment.html", data_payment)
            except ValueError as e:
                print "Errors Parse Json Verify Card : ", e
                data_payment["card_error"] = "System API Error. Please Contact Administrator."
                return render(request, "websites/metiz_payment/metiz_payment.html", data_payment)
            
        else:
            if 'card_barcode' in form_otp.errors:
                data_payment["card_error"] = "Card Barcode is required and must be number."
                return render(request, "websites/metiz_payment/metiz_payment.html", data_payment)

            return render(request, "websites/metiz_payment/payment_danger.html")

    except Exception as e:
        import traceback
        print traceback.format_exc()
        print "Errors generate_otp : ", e
        error = {
            "code": 500, "message": "System API Error. Please Contact Administrator."
        }
        raise Exception(
            "ERROR : Internal Server Error .Please contact administrator.")


def verify_otp_for_user(request):
    """ 
        Action Generate OTP for User using Metiz or Helio Payment Card 
        Step 1 : Verify session with working_id expired and amount
        Step 2 : Verify OTP
        Step 3 : Send success or fail SMS to user (phone into confirm information when booking)

    """
    try:
        print "request.POST ",request.POST
        code_otp = request.POST.get("code_otp", None)
        # Append data for form using detect request hacking
        form_otp = MetizOTPForm(request.POST)
        # init data cache for page
        data_payment = request.POST.dict()

        if not code_otp:
            data_payment['error_otp'] = "OTP is required."
            return render(request, "websites/metiz_payment/payment_verify.html", data_payment)

        # Call funtion check working_id into session exists and amount equal total_payment_store
        working_id = request.POST.get("working_id", None)
        movies_session = request.session.get("movies", "")
        

        money_store_dict = {"amount_ticket": 0, "amount_fb": 0} 
        result_check = check_amount_and_timeout(movies_session, working_id, money_store_dict)
        if not money_store_dict["amount_ticket"]:
            return result_check

        amount = money_store_dict["amount_ticket"]
        
        print "### OTP FORM ",form_otp.is_valid()
        if form_otp.is_valid():
            # Verify OTP
            secret_key_otp = movies_session[working_id]["secret_key_otp"]
            result_verify_otp =  metiz_otp.verify_otp_user(secret_key_otp, str(code_otp))
            print "result_verify_otp ",result_verify_otp
            if not result_verify_otp['status']:
                data_payment['error_otp'] = result_verify_otp['message']
                return render(request, "websites/metiz_payment/payment_verify.html", data_payment)

            order_id = form_otp.cleaned_data["order_id"]
            order_desc = form_otp.cleaned_data["order_desc"]
            seats_choice = form_otp.cleaned_data["seats_choice"]
            barcode = form_otp.cleaned_data["barcode"]
            card_barcode = form_otp.cleaned_data["card_barcode"]
            id_server  = form_otp.cleaned_data["id_server"]
            # Store order infomation with status is pendding
            booking_order = BookingInfomation(order_id=order_id, order_desc=order_desc, amount=amount, phone=request.session.get("phone", ""),
                                              email=request.session.get("email", ""), seats=seats_choice, barcode=barcode, card_barcode=card_barcode,
                                              id_server=id_server, order_status="pendding")

            if not request.user.is_anonymous():
                booking_order.user = request.user
            booking_order.save()

            url_payment_card = settings.HELIO_API_DMZ_URL + "/api/helio/card/payment/"
            # new Request Request
            data = {
                "card_barcode": form_otp.cleaned_data["card_barcode"],
                "cashier_id": "0",
                "pos_id": "0",
                "bill_number": order_id,
                "amount_ticket": money_store_dict["amount_ticket"],
                "amount_fb": money_store_dict["amount_fb"],
                "payment_value": "cash_balance",
                "system_name": "metiz_online",
                "is_verify": False
             }
            
            request_payment_card = urllib2.Request(url_payment_card, data=json.dumps(data), headers={
                                      'Content-Type': 'application/json', 'Authorization': 'Bearer %s' % settings.DMZ_API_TOKEN})

            # Call api and response data
            try:
                resp_payment_card = urllib2.urlopen(request_payment_card)
                result_payment_card = json.loads(resp_payment_card.read())
                # Begin excute payment transaction and store to booking information
                # send sms and email
                if result_payment_card["status"] == "00":
                    booking_handle.process_confirm_booking(request, booking_order, amount)
                    return render(request, "websites/vnpay_payment/payment_return.html", {"title": "Kết quả thanh toán",
                                                                                      "result": "Thành công", "order_id": order_id,
                                                                                      "amount": amount,
                                                                                      "order_desc": order_desc,
                                                                                      "vnp_TransactionNo": order_id,
                                                                                      "vnp_ResponseCode": "00",
                                                                                      "barcode": barcode})
            except urllib2.HTTPError, e:
                result_error = json.loads(e.read())
                print "EXEPTION PAYMENT CARD ", result_error
                return render(request, "websites/vnpay_payment/payment_return.html", {"title": "Kết quả thanh toán",
                                                                                      "result": "Lỗi", "order_id": order_id,
                                                                                      "amount": amount,
                                                                                      "order_desc": order_desc,
                                                                                      "vnp_TransactionNo": order_id,
                                                                                      "vnp_ResponseCode": "01",
                                                                                      "barcode": barcode,
                                                                                      "card_error": result_error["message"]})

            except ValueError as e:
                print "Errors Parse Json Payment Card : ", e
                return render(request, "websites/vnpay_payment/payment_return.html", {"title": "Kết quả thanh toán",
                                                                                      "result": "Lỗi", "order_id": order_id,
                                                                                      "amount": amount,
                                                                                      "order_desc": order_desc,
                                                                                      "vnp_TransactionNo": order_id,
                                                                                      "vnp_ResponseCode": "01",
                                                                                      "barcode": barcode})

        else:
            return render(request, "websites/metiz_payment/payment_danger.html")

    except Exception as e:
        import traceback
        print traceback.format_exc()
        print "Errors generate_otp : ", e
        error = {
            "code": 500, "message": "System API Error. Please Contact Administrator."
        }
        raise Exception(
            "ERROR : Internal Server Error .Please contact administrator.")
