# -*- coding: utf-8 -*-
from django.conf import settings
import json
import urllib
import urllib2
import requests
from django.template import loader, Context, Template
from django.utils.translation import ugettext_lazy as _
import HTMLParser



def call_api_seats(id_showtime, id_server=1):
    try:
        """ Call API get new seats of show time """
        url_get_seats = settings.BASE_URL_CINESTAR + "/getSeats"
        values = {
            "id_ShowTimes": id_showtime,
            "id_Server": id_server,
            "Secret": settings.CINESTAR_SERECT_KEY
        }
        request = urllib2.Request(url_get_seats, data=urllib.urlencode(values),
                                  headers={'Content-Type': 'application/x-www-form-urlencoded'})
        resp = urllib2.urlopen(request)
        # handle decoding json
        try:
            result = json.loads(resp.read())

        except ValueError as e:
            print "Error convert json : %s" % e
            return {"code": 500, "message": _("Handle data error.")}
    except Exception, e:
        print "Error call_api_seats : %s" % e
        result = {"List": []}
    return result


def call_api_post_booking(full_name, phone, email, seats_choice, id_server=1, url="/postBooking"):
    try:
        """ Call API get new seats of show time """
        url_booking = settings.BASE_URL_CINESTAR + url
        
        data_binding = {
            "secret": settings.CINESTAR_SERECT_KEY,
            "id_server": id_server,
            "phone": phone,
            "list_seats": str(seats_choice),
            "full_name": str(full_name).replace("<", "").replace(">", "").replace("&", "").replace("'", "").replace('\\', ""),
            "email": email

        }

        cxt = Context(data_binding)
        """ bind data to html template """
        html_parse = HTMLParser.HTMLParser()
        text_content = html_parse.unescape(loader.get_template("websites/booking/data_json.txt").render(cxt))
        
        request = urllib2.Request(url_booking, data=str(text_content),
                                  headers={'Content-Type': 'application/x-www-form-urlencoded'})
        resp = urllib2.urlopen(request)
        # handle decoding json
        try:
            result = json.loads(resp.read())

        except ValueError as e:
            print "Error convert json : %s" % e
            return {"code": 500, "message": _("Handle data error.")}
    except Exception, e:
        print "Error call_api_post_booking : %s" % e
        result = {"errors": _("Internal Server Error. Cannot Post Booking.")}
    return result


def call_api_booking_confirm(barcode, id_server=1, status=1):
    try:
        """ 
            Call API confirm booking payment success
            - status parameter : 1 is payment done, 2 cancel payment
        """
        url_confirm = settings.BASE_URL_CINESTAR + "/putBookingConfirm"
        values = {
            "Barcode": barcode,
            "Status": status,
            "id_Server": id_server,
            "Secret": settings.CINESTAR_SERECT_KEY
        }
        request = urllib2.Request(url_confirm, data=urllib.urlencode(values),
                                  headers={'Content-Type': 'application/x-www-form-urlencoded'})
        resp = urllib2.urlopen(request)
        # handle decoding json
        try:
            result = json.loads(resp.read())

        except ValueError as e:
            print "Error convert json : %s" % e
            return {"code": 500, "message": _("Handle data error.")}
    except Exception, e:
        print "Error call_api_booking_confirm : %s" % e
        result = {"errors": _("Internal Server Error. Cannot Post Booking.")}
    return result


def call_api_cancel_seat(seat_id, id_server=1):
    try:
        """ 
            Call API confirm booking payment success
            - status parameter : 1 is payment done, 2 cancel payment
        """
        url_cancel = settings.BASE_URL_CINESTAR + "/putSeatChoose"
        values = {
            "id_Seats": seat_id,
            "id_Server": id_server,
            "Secret": settings.CINESTAR_SERECT_KEY
        }
        request = urllib2.Request(url_cancel, data=urllib.urlencode(values),
                                  headers={'Content-Type': 'application/x-www-form-urlencoded'})
        resp = urllib2.urlopen(request)
        # handle decoding json
        try:
            result = json.loads(resp.read())

        except ValueError as e:
            print "Error convert json : %s" % e
            return {"code": 500, "message": _("Handle data error.")}
    except Exception, e:
        print "Error call_api_cancel_seat : %s" % e
        result = {"errors": _("Internal Server Error. Cannot Post Booking.")}
    return result
