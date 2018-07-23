from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes, api_view
from api_app import serializers
from internal_payment import metiz_otp
from core import metiz_sms
from django.http import JsonResponse
from django.conf import settings
from datetime import datetime
from core import sys_msg, metiz_cipher
from core.custom_models import User
from booking.models import BookingInfomation
from vnpay_payment.vnpay import vnpay
from vnpay_payment.views import get_client_ip



@api_view(['POST'])
@permission_classes((AllowAny,))
def payment_booking(request):
    try:
        """
            Action Payment Booking 
            Step 1: Verify Otp
            Step 2: Otp is valid then call api embeb dmz payment card
        """
        # Parameter Required : card_barcode, working_id (encrypt), data_key (serect key otp), otp
        working_id_encrypt = request.data.get('working_id', '')
        card_barcode = request.data.get('card_barcode', '')
        if not working_id_encrypt or not card_barcode:
            error = {
                "code": 400, "message": _("The working_id, card_barcode fields is required."), "fields": "working_id, card_barcode"}
            return JsonResponse(error, status=400)

        # Encrypt working_id and verify booking timeout
        cipher = MetizAESCipher()
        working_id = cipher.decrypt(str("working_id_encrypt"))
        try:
            booking_order = BookingInfomation.objects.get(working_id=working_id)
            if booking_order.order_status == 'cancel':
                error = {
                    "code": 400, "message": _("Transaction Timeout"), "fields": ""}
                return JsonResponse(error, status=400)
        except BookingInfomation.DoesNotExist, e:
            error = {
                "code": 400, "message": _("Transaction Invalid"), "fields": ""}
            return JsonResponse(error, status=400)


        # Call action verify otp
        resp_verify_otp = verify_otp(request)
        if not result_verify_otp['status']:
            return JsonResponse(resp_verify_otp, status=400)

        # update payment card to booking payment
        booking_order.card_barcode = card_barcode
        booking_order.save()

        url_payment_card = settings.HELIO_API_DMZ_URL + "/api/helio/card/payment/"

        # new Request Request
        data = {
            "card_barcode": card_barcode,
            "cashier_id": "0",
            "pos_id": "0",
            "bill_number": booking_order.order_id,
            "amount_ticket": booking_order.amount,
            "amount_fb": 0,
            "payment_value": "cash_balance",
            "system_name": "metiz_app",
            "is_verify": False,
            "gate_payment": booking_order.payment_gate
         }
        
        data_result = {
                        "order_id": booking_order.order_id,
                        "amount": booking_order.amount,
                        "order_desc": booking_order.order_desc,
                        "barcode": booking_order.barcode
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
                return JsonResponse(data_result)

        except urllib2.HTTPError, e:
            result_error = json.loads(e.read())
            print "EXEPTION PAYMENT CARD ", result_error
            data_result["card_error"] = result_error["message"]
            return JsonResponse(data_result, status=400)
            
        except ValueError as e:
            print "Errors Parse Json Payment Card : ", e
            return JsonResponse(data_result, status=400)
    except:
        print('Error Rest API payment_booking: %s', traceback.format_exc())
        error = {"code": 500, "message": "ERROR : Internal Server Error .Please contact administrator.", "fields": ""}
        return JsonResponse(error, status=500)


@api_view(['POST'])
@permission_classes((AllowAny,))
def payment_method(request):
    try:
        """ 
            Action Update gate payment method for booking information.
            Return url if method is VNPay
        """
        gate_payment = request.data.get('gate_payment')
        working_id_encrypt = request.data.get('working_id', '')
        if not gate_payment or not working_id_encrypt:
            error = {
                "code": 400, "message": _("The gate_payment, working_id fields is required."), "fields": "gate_payment, working_id"}
            return JsonResponse(error, status=400)

        # Encrypt working_id and verify booking timeout
        cipher = MetizAESCipher()
        working_id = cipher.decrypt(str("working_id_encrypt"))
        try:
            booking_order = BookingInfomation.objects.get(working_id=working_id)
            if booking_order.order_status == 'cancel':
                error = {
                    "code": 400, "message": _("Transaction Timeout"), "fields": ""}
                return JsonResponse(error, status=400)

            # update gate payment
            booking_order.gate_payment = gate_payment
            booking_order.save()
        except BookingInfomation.DoesNotExist, e:
            error = {
                "code": 400, "message": _("Transaction Invalid"), "fields": ""}
            return JsonResponse(error, status=400)

        result = {'code': 200, "url":""}
        if gate_payment == "VNPay":
             # Build URL Payment
            vnp = vnpay()
            vnp.requestData['vnp_Version'] = '2.0.0'
            vnp.requestData['vnp_Command'] = 'pay'
            vnp.requestData['vnp_TmnCode'] = settings.VNPAY_TMN_CODE
            vnp.requestData['vnp_Amount'] = int(booking_order.amount) * 100
            vnp.requestData['vnp_CurrCode'] = 'VND'
            vnp.requestData['vnp_TxnRef'] = booking_order.order_id
            vnp.requestData['vnp_OrderInfo'] = booking_order.order_desc
            vnp.requestData['vnp_OrderType'] = "190001"
            vnp.requestData['vnp_Locale'] = 'vn'
        
            vnp.requestData['vnp_CreateDate'] = datetime.now(
            ).strftime('%Y%m%d%H%M%S')  # 20150410063022
            vnp.requestData['vnp_IpAddr'] = get_client_ip(request)
            vnp.requestData['vnp_ReturnUrl'] = settings.VNPAY_RETURN_URL
            vnpay_payment_url = vnp.get_payment_url(
                settings.VNPAY_PAYMENT_URL, settings.VNPAY_HASH_SECRET_KEY)

            result["url"] = vnpay_payment_url

        return JsonResponse(result)
    except Exception, e:
        print('Error Rest API payment_method: %s', traceback.format_exc())
        error = {"code": 500, "message": "ERROR : Internal Server Error .Please contact administrator.", "fields": ""}
        return JsonResponse(error, status=500)


@api_view(['POST'])
@permission_classes((AllowAny,))
def verify_payment_card(request):
    try:
        print "### Rest API verify_payment_card "
        card_barcode = request.data.get('card_barcode', '')
        working_id_encrypt = request.data.get('working_id', '')
        if not card_barcode or not working_id_encrypt:
            error = {
                "code": 400, "message": _("The card_barcode, working_id field is required."), "fields": "card_barcode, working_id"}
            return JsonResponse(error, status=400)

        # Decrypt working_id and verify transaction timeout when status is cancel
        cipher = MetizAESCipher()
        working_id = cipher.decrypt(str("working_id_encrypt"))
        try:
            booking_order = BookingInfomation.objects.get(working_id=working_id)
            if booking_order.order_status == 'cancel':
                error = {
                    "code": 400, "message": _("Transaction Timeout"), "fields": ""}
                return JsonResponse(error, status=400)    
        except BookingInfomation.DoesNotExist, e:
            error = {
                "code": 400, "message": _("Transaction Invalid"), "fields": ""}
            return JsonResponse(error, status=400)


        # Call embeb dmz verify card barcode
        url_verify_card = settings.HELIO_API_DMZ_URL + "/api/helio/card/payment/"
        amount_fb = 0
        amount_ticket = booking_order.amount
        data = {
            "card_barcode": card_barcode,
            "cashier_id": "0",
            "pos_id": "0",
            "bill_number": booking_order.order_id,
            "amount_ticket": amount_ticket,
            "amount_fb": amount_fb,
            "payment_value": "cash_balance",
            "system_name": "metiz_app",
            "is_verify": True,
            "gate_payment": booking_order.gate_payment
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
            print "### OTP generate ",code_otp
            if code_otp["code_otp"] == "000000":
                error = {"code": 500, "message": "ERROR : Internal Server Error .Please contact administrator.", "fields": ""}
                return JsonResponse(error, status=500)

            # Begin send SMS OTP for User
            sms_otp = sys_msg.MSG_SMS_OTP%(amount_ticket, str(code_otp["code_otp"]))
            metiz_sms.send_sms(phone_number, sms_otp)

            # hidden phone suggest for user
            result['data_key'] = cipher.encrypt(code_otp["secret_key_otp"])
            result['phone'] = cipher.encrypt(str(phone_number))
            
            phone_hide = phone_number[:3] + 'xxxx' + phone_number[-3:]
            result['phone_hide'] = phone_hide
            result['amount'] = amount_ticket + amount_fb
            result['code'] = 200
            return JsonResponse(result)

        except urllib2.HTTPError, e:
            result_error = json.loads(e.read())
            print "Rest API EXEPTION VERIFY CARD ", result_error
            result["card_error"] = result_error["message"]
            return JsonResponse({"card_error": result_error["message"]}, status=400)
        except ValueError as e:
            print "REST API Errors Parse Json Verify Card : ", e
            return JsonResponse({"card_error": _("System Error. Please Contact Administrator.")}, status=400)

    except Exception, e:
        print('Error verify_payment_card: %s', traceback.format_exc())
        error = {"code": 500, "message": "ERROR : Internal Server Error .Please contact administrator.", "fields": ""}
        return JsonResponse(error, status=500)


@api_view(['POST'])
@permission_classes((AllowAny,))
def forgot_password(request):
    try:
        # validate email is required
        email = request.data.get('email', '')
        if not email:
            error = {
                "code": 400, "message": _("The email field is required."), "fields": "email"}
            return JsonResponse(error, status=400)

        try:
            user_obj = User.objects.get(email=email)
            phone_number = user_obj.phone
        except User.DoesNotExist, e:
            return JsonResponse(
                    {'code': 200, 'Message': 'Process data success', 'data': ""})

        # Call action generate opt and return serect key opt encrypt for client
        code_otp = metiz_otp.opt_user()
        if code_otp["code_otp"] == "000000":
            error = {
                "code": 400, "message": _("System Error. Please Contact Administrator."), "fields": "code"}
            return JsonResponse(error, status=400)
        
        # send otp code via sms for user
        sms_otp = sys_msg.FORGOT_PASS_MSG_SMS_OTP%(str(code_otp["code_otp"]))
        metiz_sms.send_sms(phone_number, sms_otp)

        # Ecrypt serect key otp
        cipher = MetizAESCipher()
        key_encrypted = cipher.encrypt(str(code_otp["secret_key_otp"]))
        phone_encrypt = cipher.encrypt(str(phone_number))
        return JsonResponse(
                    {'code': 200, 'data_key': key_encrypted, 'phone':phone_encrypt})
    except Exception, e:
        print('Error forgot_password: %s', traceback.format_exc())
        error = {"code": 500, "message": "ERROR : Internal Server Error .Please contact administrator.", "fields": ""}
        return JsonResponse(error, status=500)



@api_view(['POST'])
@permission_classes((AllowAny,))
def resend_otp(request):
    try:
        phone_encrypt = request.data.get('phone', '')
        is_payment = request.data.get('is_payment', False)
        amount = request.data.get('amount', 0)
        if not phone_encrypt:
            error = {
                "code": 400, "message": _("The phone field is required."), "fields": "phone"}
            return JsonResponse(error, status=400)

        cipher = MetizAESCipher()
        phone_number = cipher.decrypt(str(phone))
        
        code_otp = metiz_otp.opt_user()
        if code_otp["code_otp"] == "000000":
            error = {
                "code": 400, "message": _("System Error. Please Contact Administrator."), "fields": "code"}
            return JsonResponse(error, status=400)
        
        if is_payment:
            sms_otp = sys_msg.MSG_SMS_OTP%(amount, str(code_otp["code_otp"]))
        else:
            sms_otp = sys_msg.FORGOT_PASS_MSG_SMS_OTP%(str(code_otp["code_otp"]))

        metiz_sms.send_sms(phone_number, sms_otp)

        key_encrypted = cipher.encrypt(str(code_otp["secret_key_otp"]))
        return JsonResponse({'code': 200, 'data_key': key_encrypted})

    except Exception, e:
        print('Error verify_otp: %s', traceback.format_exc())
        error = {"code": 500, "message": "ERROR : Internal Server Error .Please contact administrator.", "fields": ""}
        return JsonResponse(error, status=500)        



@api_view(['POST'])
@permission_classes((AllowAny,))
def verify_otp(request):
    try:
        secret_key_encrypt = request.data.get('data_key', '')
        code_otp = request.data.get('code_otp', '')
        if not secret_key_otp or not code_otp:
            error = {
                "code": 400, "message": _("The code_otp and data_key fields is required."), "fields": "code_otp, data_key"}
            return JsonResponse(error, status=400)

        cipher = MetizAESCipher()
        secret_key_otp = cipher.decrypt(str(code_otp["secret_key_encrypt"]))
        
        result_verify_otp =  metiz_otp.verify_otp_user(secret_key_otp, str(code_otp))
        
        if not result_verify_otp['status']:
            error = {"code": 500, "message": "ERROR : Internal Server Error .Please contact administrator.", "fields": ""}
            return JsonResponse(error, status=500)        
        
        return JsonResponse(result_verify_otp)

    except Exception, e:
        print('Error verify_otp: %s', traceback.format_exc())
        error = {"code": 500, "message": "ERROR : Internal Server Error .Please contact administrator.", "fields": ""}
        return JsonResponse(error, status=500)        


