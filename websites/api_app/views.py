from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from core.models import *
from core.custom_models import User
from core.metiz_cipher import MetizAESCipher
from core import sys_msg
from api_app import serializers
from registration import forms as forms_registration
from api import actions
from booking import api
import json

# Create your views here.


# Author: Lam
@api_view(['POST'])
@permission_classes((AllowAny, ))
def register(request):
    """
        - Use forms_registration from registration form
        - Return serialzer data
    """
    register_form = forms_registration.MetizSignupForm(request.data, request=request)

    if register_form.is_valid():
        register_form.save()
        return Response({"message": _('Register Account Successfully. Please Check Your Email and Active Account.')})

    return Response({'errors': register_form.errors}, status=400)


# Author: Lam
@permission_classes((AllowAny, ))
class BlogViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = Blog.objects.filter(is_draft=False).order_by('-created', '-id')
    serializer_class = serializers.BlogSerializer


# Author: Lam
@permission_classes((AllowAny, ))
class FaqViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = FAQ_Category.objects.all()
    serializer_class = serializers.FaqCategorySerializer


# Author: Lam
class TransactionHistoryList(ListAPIView):

    def get(self, request, format=None):
        try:
            user_id = request.user.id
            lst_item = actions.get_booking_info_data(user_id, None, None, {'done'})
            return Response(lst_item['results'])

        except Exception, e:
            print 'TransactionHistoryList ', e
            error = {"code": 500, "message": _(
                "Internal Server Error"), "fields": ""}
            return Response(error, status=500)


# Author: Lam
class ProfileDetail(RetrieveUpdateAPIView):

    def get_card_member(self, user):
        # Get link card by user
        linkcard = LinkCard.objects.filter(user=user)
        # if user in link then get first linked
        card_member = linkcard.first().card_member if linkcard else ''
        return card_member


    def get(self, request, format=None):
        try:
            user = request.user
            card_member = self.get_card_member(user)
            serializer_user = serializers.ProfileSerializer(user, many=False)
            return Response({"user": serializer_user.data, "card_member": card_member})

        except Exception, e:
            print 'ProfileDetail ', e
            error = {"code": 500, "message": _(
                "Internal Server Error"), "fields": ""}
            return Response(error, status=500)


    def put(self, request, format=None):
        try:
            user = request.user
            profile_form = forms_registration.UpdateUserForm(request.data, user=user)
            if profile_form.is_valid():
                profile_data = profile_form.save()
                serializer = serializers.ProfileSerializer(profile_data, many=False)
                return Response(serializer.data)
            return Response({"code": 400, "message": profile_form.errors, "fields": ""}, status=400)

        except Exception, e:
            print 'ProfileDetail PUT', e
            error = {"code": 500, "message": _(
                "Internal Server Error"), "fields": ""}
            return Response(error, status=500)



"""
    Function get_movie_seat
    Author: HoangNguyen
    Duplication: get_seats
"""


@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_movie_seat(request):
    try:
        id_server = request.query_params.get('id_server', 1)
        id_showtime = request.query_params.get('id_showtime', None)

        if id_showtime:
            result = api.call_api_seats(id_showtime, id_server)
            return Response(result)
        error = {"code": 400, "message": _("Field id_showtime is required."),
                 "fields": "id_showtime"}
        return Response(error, status=400)
    except Exception, e:
        print "Error get_movie_seat : %s" % e
        return Response({"code": 500, "message": _("Internal Server Error. Please contact administrator.")}, status=500)

"""
    Function check_movie_seat
    Author: HoangNguyen
    Duplication: check_seats

"""


@api_view(['POST'])
@permission_classes((AllowAny, ))
def check_movie_seat(request):
    try:
        id_server = request.data.get('id_server', 1)
        id_showtime = request.data.get('id_showtime', None)
        seats_choice = request.data.get('seats_choice', None)

        if not seats_choice or not id_showtime:
            error = {"code": 400, "message": _("Fields id_showtime, seats_choice is required."),
                     "fields": "id_showtime, seats_choice"}
            return Response(error, status=400)
        data_seats = api.call_api_seats(id_showtime, id_server)

        if data_seats and data_seats["List"]:
            # step 1.Check seat is selected
            seat_has_selected = []
            total_money = 0
            for item in seats_choice:
                chair_is_choice = [str(s["NAME"]) for s in data_seats["List"] if s[
                    "ID"] == item["ID"] and s["STATUS"] == "True"]
                total_money += sum(int(s["PRICE"]) for s in data_seats["List"] if s[
                    "ID"] == item["ID"])
                if chair_is_choice:
                    seat_has_selected.append(chair_is_choice[0])

            if seat_has_selected:
                return Response({"code": 400, "message": _("These chairs have been selected ") + str(seat_has_selected)}, status=400)

            # step 2.Lock seat
            full_name = request.data.get('full_name', None)
            phone = request.data.get('phone', None)
            email = request.data.get('email', None)

            if not full_name or not phone:
                error = {"code": 400, "message": _("Fields full_name, phone is required."),
                         "fields": "id_showtime, seats_choice"}
                return Response(error, status=400)
            # remove uni
            seats_choice_clean = json.dumps(seats_choice)
            url = "/postBooking"
            result = api.call_api_post_booking(
                full_name, phone, email, seats_choice_clean, id_server, None, url)

            if not result["BARCODE"] or str(result["BARCODE"]) == '0' or total_money <= 0:
                print "***** Get Barcode Fail : ", result
                return Response({"code": 400, "message": _("Cannot Booking Seats. Please Contact Administrator.")}, status=400)

            # step 3.Save bookingInfomation
            seats = str([int(item['ID']) for item in seats_choice]).strip('[]')
            bookingSerializer = serializers.BookingInfomationSerializer(data=request.data, context={
                                                                        'amount': total_money, 'seats': seats, 'barcode': result["BARCODE"]})
            if bookingSerializer.is_valid():
                bookingSerializer.save()
                return Response(bookingSerializer.data)
            return Response(bookingSerializer.errors, status=400)
        return Response({"code": 400, "message": _("Not found showtime for id_showtime")}, status=400)

    except Exception, e:
        print "Error check_movie_seat : %s" % e
        return Response({"code": 500, "message": _("Internal Server Error. Please contact administrator.")}, status=500)


"""
    Author: TienDang
"""
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
            return Response(error, status=400)

        # Encrypt working_id and verify booking timeout
        cipher = MetizAESCipher()
        working_id = cipher.decrypt(str("working_id_encrypt"))
        try:
            booking_order = BookingInfomation.objects.get(working_id=working_id)
            if booking_order.order_status == 'cancel':
                error = {
                    "code": 400, "message": _("Transaction Timeout"), "fields": ""}
                return Response(error, status=400)
        except BookingInfomation.DoesNotExist, e:
            error = {
                "code": 400, "message": _("Transaction Invalid"), "fields": ""}
            return Response(error, status=400)


        # Call action verify otp
        resp_verify_otp = verify_otp(request)
        if not result_verify_otp['status']:
            return Response(resp_verify_otp, status=400)

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
                return Response(data_result)

        except urllib2.HTTPError, e:
            result_error = json.loads(e.read())
            print "EXEPTION PAYMENT CARD ", result_error
            data_result["card_error"] = result_error["message"]
            return Response(data_result, status=400)
            
        except ValueError as e:
            print "Errors Parse Json Payment Card : ", e
            return Response(data_result, status=400)
    except:
        print('Error Rest API payment_booking: %s', traceback.format_exc())
        error = {"code": 500, "message": "ERROR : Internal Server Error .Please contact administrator.", "fields": ""}
        return Response(error, status=500)


"""
    Author: TienDang
"""
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
            return Response(error, status=400)

        # Encrypt working_id and verify booking timeout
        cipher = MetizAESCipher()
        working_id = cipher.decrypt(str("working_id_encrypt"))
        try:
            booking_order = BookingInfomation.objects.get(working_id=working_id)
            if booking_order.order_status == 'cancel':
                error = {
                    "code": 400, "message": _("Transaction Timeout"), "fields": ""}
                return Response(error, status=400)

            # update gate payment
            booking_order.gate_payment = gate_payment
            booking_order.save()
        except BookingInfomation.DoesNotExist, e:
            error = {
                "code": 400, "message": _("Transaction Invalid"), "fields": ""}
            return Response(error, status=400)

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

        return Response(result)
    except Exception, e:
        print('Error Rest API payment_method: %s', traceback.format_exc())
        error = {"code": 500, "message": "ERROR : Internal Server Error .Please contact administrator.", "fields": ""}
        return Response(error, status=500)


"""
    Author: TienDang
"""
@api_view(['POST'])
@permission_classes((AllowAny,))
def verify_payment_card(request):
    try:
        """
            Action Verify Card Payment
            Step 1 : Check booking data timeout by working_id
            Step 2 : Call embeb dmz verify card payment
            Step 3 : Send Otp for user and encrypt phone return for client
        """
        print "### Rest API verify_payment_card "
        card_barcode = request.data.get('card_barcode', '')
        working_id_encrypt = request.data.get('working_id', '')
        if not card_barcode or not working_id_encrypt:
            error = {
                "code": 400, "message": _("The card_barcode, working_id field is required."), "fields": "card_barcode, working_id"}
            return Response(error, status=400)

        # Decrypt working_id and verify transaction timeout when status is cancel
        cipher = MetizAESCipher()
        working_id = cipher.decrypt(str("working_id_encrypt"))
        try:
            booking_order = BookingInfomation.objects.get(working_id=working_id)
            if booking_order.order_status == 'cancel':
                error = {
                    "code": 400, "message": _("Transaction Timeout"), "fields": ""}
                return Response(error, status=400)    
        except BookingInfomation.DoesNotExist, e:
            error = {
                "code": 400, "message": _("Transaction Invalid"), "fields": ""}
            return Response(error, status=400)


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
                return Response(error, status=500)

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
            return Response(result)

        except urllib2.HTTPError, e:
            result_error = json.loads(e.read())
            print "Rest API EXEPTION VERIFY CARD ", result_error
            result["card_error"] = result_error["message"]
            return Response({"card_error": result_error["message"]}, status=400)
        except ValueError as e:
            print "REST API Errors Parse Json Verify Card : ", e
            return Response({"card_error": _("System Error. Please Contact Administrator.")}, status=400)

    except Exception, e:
        print('Error verify_payment_card: %s', traceback.format_exc())
        error = {"code": 500, "message": "ERROR : Internal Server Error .Please contact administrator.", "fields": ""}
        return Response(error, status=500)


"""
    Author: TienDang
"""
@api_view(['POST'])
@permission_classes((AllowAny,))
def forgot_password(request):
    try:
        """
            Action Recovery Password via email
            Step 1 : Get user by email
            Step 2 : Send Otp for user via phone number
            Step 3 : Encrypt serect key otp and phone return for client
        """
        # validate email is required
        email = request.data.get('email', '')
        if not email:
            error = {
                "code": 400, "message": _("The email field is required."), "fields": "email"}
            return Response(error, status=400)

        try:
            user_obj = User.objects.get(email=email)
            phone_number = user_obj.phone
        except User.DoesNotExist, e:
            return Response(
                    {'code': 200, 'Message': 'Process data success', 'data': ""})

        # Call action generate opt and return serect key opt encrypt for client
        code_otp = metiz_otp.opt_user()
        if code_otp["code_otp"] == "000000":
            error = {
                "code": 400, "message": _("System Error. Please Contact Administrator."), "fields": "code"}
            return Response(error, status=400)
        
        # send otp code via sms for user
        sms_otp = sys_msg.FORGOT_PASS_MSG_SMS_OTP%(str(code_otp["code_otp"]))
        metiz_sms.send_sms(phone_number, sms_otp)

        # Ecrypt serect key otp
        cipher = MetizAESCipher()
        key_encrypted = cipher.encrypt(str(code_otp["secret_key_otp"]))
        phone_encrypt = cipher.encrypt(str(phone_number))
        return Response(
                    {'code': 200, 'data_key': key_encrypted, 'phone':phone_encrypt})
    except Exception, e:
        print('Error forgot_password: %s', traceback.format_exc())
        error = {"code": 500, "message": "ERROR : Internal Server Error .Please contact administrator.", "fields": ""}
        return Response(error, status=500)



"""
    Author: TienDang
"""
@api_view(['POST'])
@permission_classes((AllowAny,))
def resend_otp(request):
    try:
        """
            Action Resend OTP
            Step 1 : Verify Phone is required.
            Step 2 : Generate OTP and serect key
            Step 3 : Encrypt serect key and return for client
        """
        phone_encrypt = request.data.get('phone', '')
        is_payment = request.data.get('is_payment', False)
        amount = request.data.get('amount', 0)
        if not phone_encrypt:
            error = {
                "code": 400, "message": _("The phone field is required."), "fields": "phone"}
            return Response(error, status=400)

        cipher = MetizAESCipher()
        phone_number = cipher.decrypt(str(phone))
        
        code_otp = metiz_otp.opt_user()
        if code_otp["code_otp"] == "000000":
            error = {
                "code": 400, "message": _("System Error. Please Contact Administrator."), "fields": "code"}
            return Response(error, status=400)
        
        if is_payment:
            sms_otp = sys_msg.MSG_SMS_OTP%(amount, str(code_otp["code_otp"]))
        else:
            sms_otp = sys_msg.FORGOT_PASS_MSG_SMS_OTP%(str(code_otp["code_otp"]))

        metiz_sms.send_sms(phone_number, sms_otp)

        key_encrypted = cipher.encrypt(str(code_otp["secret_key_otp"]))
        return Response({'code': 200, 'data_key': key_encrypted})

    except Exception, e:
        print('Error verify_otp: %s', traceback.format_exc())
        error = {"code": 500, "message": "ERROR : Internal Server Error .Please contact administrator.", "fields": ""}
        return Response(error, status=500)        



"""
    Author: TienDang
"""
@api_view(['POST'])
@permission_classes((AllowAny,))
def verify_otp(request):
    try:
        """
            Action Verify OTP
            Step 1 : Verify serect key and otp is required.
            Step 2 : Decrypt serect key
            Step 3 : Verify OTP by serect key
        """
        secret_key_encrypt = request.data.get('data_key', '')
        code_otp = request.data.get('code_otp', '')
        if not secret_key_otp or not code_otp:
            error = {
                "code": 400, "message": _("The code_otp and data_key fields is required."), "fields": "code_otp, data_key"}
            return Response(error, status=400)

        cipher = MetizAESCipher()
        secret_key_otp = cipher.decrypt(str(code_otp["secret_key_encrypt"]))
        
        result_verify_otp =  metiz_otp.verify_otp_user(secret_key_otp, str(code_otp))
        
        if not result_verify_otp['status']:
            error = {"code": 500, "message": "ERROR : Internal Server Error .Please contact administrator.", "fields": ""}
            return Response(error, status=500)        
        
        return Response(result_verify_otp)

    except Exception, e:
        print('Error verify_otp: %s', traceback.format_exc())
        error = {"code": 500, "message": "ERROR : Internal Server Error .Please contact administrator.", "fields": ""}
        return Response(error, status=500)

