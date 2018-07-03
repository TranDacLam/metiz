# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.conf import settings
from django.http import JsonResponse
from core.models import AdminInfo
from registration import metiz_email
from core import metiz_sms
from booking import api
import urllib2
import json

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
            'site': str(Site.objects.get_current()),
            'HOT_LINE': settings.HOT_LINE
        }
        # Send email booking success
        metiz_email.send_mail(subject, None, message_html, settings.DEFAULT_FROM_EMAIL, [
                              email], data_binding)
    except Exception, e:
        print "Error send_mail_booking : ", e

def send_mail_booking_error(is_secure, email, email_cc, barcode, content):
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
            'site': str(Site.objects.get_current()),
            'HOT_LINE': settings.HOT_LINE
        }
        # Send email transaction booking moive order error
        metiz_email.send_mail(subject, None, message_html, settings.DEFAULT_FROM_EMAIL, [
                              email], data_binding, {} , (), None, email_cc)
    except Exception, e:
        print "Error send_mail_booking : ", e

def send_mail_point_errors(is_secure, email, email_cc, barcode, content, fullname):
    try:
        message_html = "websites/booking/email/add_point_error.html"
        subject = _("[Metiz] Accumulation Point for Tickets Error !")

        protocol = 'http'
        if is_secure:
            protocol = 'https'
        logo_url = '/static/assets/websites/images/logo_bottom.png'
        data_binding = {
            "protocol": protocol,
            'URL_LOGO': logo_url,
            'barcode': barcode,
            'content': content,
            'site': str(Site.objects.get_current()),
            'HOT_LINE': settings.HOT_LINE,
            'fullname': fullname
        }
        # Send email transaction booking moive order error
        metiz_email.send_mail(subject, None, message_html, settings.DEFAULT_FROM_EMAIL, [
                              email], data_binding, {} , (), None, email_cc)
    except Exception, e:
        print "Error send_mail_booking : ", e

def send_mail_amount_not_match(is_secure, email, full_name, barcode, content):
    try:
        message_html = "websites/booking/email/warning_amount_payment.html"
        subject = _("[Metiz] Warning Payment Amount not Match")

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
            'site': str(Site.objects.get_current()),
            'HOT_LINE': settings.HOT_LINE
        }
        # Send email booking success
        metiz_email.send_mail(subject, None, message_html, settings.DEFAULT_FROM_EMAIL, [
                              email], data_binding)
    except Exception, e:
        print "Error send_mail_booking : ", e


def send_email_vooc_leader(is_secure, full_name, barcode, content):
    try:
        leader_email = settings.VOOC_LEADER_EMAIL
        send_mail_amount_not_match(is_secure, leader_email, full_name, barcode, content)
    except Exception, e:
        leader_email = "tiendangdht@gmail.com, thangnguyen@vooc.vn"



def handler_error_point_bonus(booking_order, amount, is_secure):
    params = {
        "card_member": booking_order.card_member,
        "amount": amount,
        "type_payment": "tickets",
        "system_name": "metiz_web_online"
    }
    # Get link call api 
    url_add_point_to_card = '{}member/card/point/'.format(
        settings.BASE_URL_POS_API)
    
    # Call POS add point to card member
    request_calculated_point = urllib2.Request(url_add_point_to_card, data=json.dumps(params), headers={
                                  'Content-Type': 'application/json', 'Authorization': '%s' % settings.POS_API_AUTH_HEADER})

    # Call api and response data
    try:
        resp = urllib2.urlopen(request_calculated_point)
        result_point_card = json.loads(resp.read())
        booking_order.point_bonus = result_point_card['point_bonus']
        booking_order.point_level = result_point_card['point_level']
        booking_order.save()

        if not result_point_card['status_point_bonus']:
            content_user = """
                            Không tìm thấy mã thành viên để tích điểm thưởng. 
                            Vui lòng liên hệ bộ phận vận hành để kiểm tra lại. 
                            Thông tin giao dịch: Mã Đặt Vé: %s, Mã Thành Viên: %s.
                        """%(booking_order.barcode, booking_order.card_member)
            send_mail_point_errors(is_secure, booking_order.email, None, booking_order.barcode, content_user, "")

        send_point_error = False
        if not result_point_card['status_point_level']:
            send_point_error = True

    except urllib2.HTTPError, e:
        print "EXEPTION add point to card member ", e.code
        if e.code != 400:
            send_point_error = True
        pass
    
    if send_point_error:
        content_admin = """
                        Xãy ra lỗi trong quá trình tích điểm thưởng cho thành viên. 
                        Vui lòng kiểm tra lại. 
                        Thông tin giao dịch: Mã Đặt Vé: %s, Mã Thành Viên: %s.
                    """%(booking_order.barcode, booking_order.card_member)
        send_mail_point_errors(is_secure, settings.POS_ADMIN_EMAIL, None, booking_order.barcode, content_admin, "Admin Metiz Cinema")
        


def handler_confirm_booking_error(booking_order, error_comfirm, is_secure):
    if error_comfirm:
        # update number retry ipn
        booking_order.order_status = 'confirm_error'
        booking_order.desc_transaction = "Payment success but confirm booking error"
        booking_order.save()
        
        
        # Payment Error: cancel seats chooice and return for
        # vnpayment
        # if booking_order.seats:
        #     cancel_seats(booking_order.seats.split(
        #         ","), booking_order.id_server)

        # Get information admin metiz cinema
        email_admin_cinema = settings.SYSTEM_ADMIN_CINEMA_EMAIL
        email_admin_cinema_cc = settings.SYSTEM_ADMIN_CINEMA_EMAIL_CC
        phone_admin = settings.SYSTEM_ADMIN_CINEMA_PHONE

        admin_info = AdminInfo.objects.all()
        if admin_info:
            # Set phone of first row
            phone_admin = admin_info[0].phone

            # Get admin info of email to
            admin_info_to = AdminInfo.objects.filter(email_type='to')
            if admin_info_to:
                # Get string of list email to
                email_admin_cinema = ', '.join(list(admin_info_to.values_list('email', flat=True)))

            # Get admin info of email cc
            admin_info_cc = AdminInfo.objects.filter(email_type='cc')
            if admin_info_cc: 
                # Get list email cc
                email_admin_cinema_cc = list(admin_info_cc.values_list('email', flat=True))

        

        # send sms for client about transaction booking movie error.
        error_sms = """Dat ve khong thanh cong tai Metiz Cinema .Vui long lien he: %s, neu ban van chua duoc hoan tien. Ma giao dich: %s""" %(phone_admin, booking_order.order_id)
        # Send SMS notification for user transaction error
        metiz_sms.send_sms(booking_order.phone, error_sms)

        content_error = """Lỗi: Đã trừ tiền của khách hàng nhưng không thể xuất vé phim. 
                            Vui Lòng kiểm tra hoá đơn : %s để hoàn tiền hoặc xử lý vé cho khách hàng. 
                            Thông tin khách hàng: Phone: 0%s, Email: %s"""%(booking_order.order_id, booking_order.phone, booking_order.email)
        # Send email notification for admin transaction error
        print "### email_admin_cinema ",email_admin_cinema
        if email_admin_cinema:
            send_mail_booking_error(is_secure, email_admin_cinema, email_admin_cinema_cc, booking_order.barcode, content_error)
            
        return JsonResponse({'RspCode': '02', 'Message': 'Process Confirm Booking Movie Error'})


def handler_confirm_booking_success(request, booking_order, amount):
    """ Handle for vnpayemnt ipn call and process booking success"""
    booking_order.order_status = "done"
    booking_order.save()

    content_sms = """Ban da dat ve thanh cong tai Metiz Cinema. Ma dat ve: %s, """ % booking_order.barcode
    content_sms += str(booking_order.order_desc.replace("\r\n", ""))
    # Send SMS for user
    metiz_sms.send_sms(booking_order.phone, content_sms)

    # Send Email
    if booking_order.email:
        send_mail_booking(request.is_secure(), booking_order.email, request.session.get(
            "full_name", ""), booking_order.barcode, booking_order.order_desc)

    # Amount Divisoon for 100 because vnpay return amount * 100
    if booking_order.gate_payment == "VNPay":
        amount = float(amount)/100

    # Begin calculated point bonus for member
    if booking_order.card_member:
        handler_error_point_bonus(booking_order, amount, request.is_secure())

    if amount != booking_order.amount:
        content_warning = """
            Please check warning metiz payment below
            Barcode : %s
            Payment amount : %s not match with Booking Amount: %s

        """%(booking_order.barcode, float(amount)/100, booking_order.amount)
        send_email_vooc_leader(request.is_secure(), "Vooc Company", booking_order.barcode, content_warning)


def process_confirm_booking(request, booking_order, amount):
    print('Payment Gate Web-online Success. Processing Booking Confirm')
    id_server = booking_order.id_server if booking_order.id_server else 1
    # Payment Success update order status and  call api confirm
    # booking order
    result_confirm = api.call_api_booking_confirm(
        booking_order.barcode, id_server)
    
    print "#### Confirm Booking Information: Barcode : %s, status: %s"%(booking_order.barcode, result_confirm)
    # Handle Confirm Booking Error
    # ReCall confirm booking three times when booking confirm error
    recall = 1
    status_confirm = result_confirm["SUCCESS"].lower()
    error_comfirm = False if status_confirm == 'true' else True
    
    while status_confirm == 'false' and recall <= 3:
        # recall api confirm booking
        result_confirm = api.call_api_booking_confirm(
             booking_order.barcode, id_server)
        
        print "#### Confirm Booking Information %s : Barcode : %s, status: %s "%(recall, booking_order.barcode, result_confirm) 
        # update new status of api
        status_confirm = result_confirm["SUCCESS"].lower()
        error_comfirm = False if status_confirm == 'true' else True
        recall +=1

    
    if settings.DEBUG_CONFIRM_BOOKING:
        handler_confirm_booking_error(booking_order, True, request.is_secure())
    else:
        handler_confirm_booking_error(booking_order, error_comfirm, request.is_secure())


    # Handle Confirm Booking Success and send sms or email
    if not error_comfirm:
        handler_confirm_booking_success(request, booking_order, amount)

    working_id = booking_order.working_id
    print 'working_id::', working_id
    movies_session = request.session.get("movies", "")
    if movies_session and working_id in movies_session:
        del request.session['movies'][working_id]