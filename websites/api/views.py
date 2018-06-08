from django.shortcuts import render
from booking.models import BookingInfomation
from datetime import timedelta, datetime, time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
import serializers
import json
from rest_framework.decorators import api_view
from api import actions
# Create your views here.
import traceback
import requests
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from core.models import *
from dateutil.parser import parse
from django.db.models import Q

@api_view(['GET'])
def get_booking_info_report(request):
    print "Get booking online Data"
    try:
        booking_info_list = BookingInfomation.objects.all().order_by('-created')

        # Get Parameter From GET request
        order_id = request.GET.get("order_id", "")
        order_status = request.GET.getlist("order_status", "")
        email = request.GET.get("email", "")
        phone = request.GET.get("phone", "")
        barcode = request.GET.get("barcode", "")
        date_from = request.GET.get("date_from", "")
        date_to = request.GET.get("date_to", "")
        page_items = request.GET.get("page_items", 0)
        page_number = request.GET.get("page_number", 1)

        # Call action get data response
        responses = actions.get_booking_info_data(None, page_items, page_number, order_status,
                                                  order_id, email, phone, barcode, date_from, date_to)
        # Return data with json
        return JsonResponse(responses['results'], status=responses["status"], safe=responses["safe"])

    except Exception, e:
        print "Error booking_info_report : %s ", traceback.format_exc()
        raise Exception(
            "ERROR : Internal Server Error .Please contact administrator.")


"""
    Get gift claiming points
"""


@api_view(['GET'])
def get_gift_claiming_points(request):
    print "Get gift claiming points"
    try:
        headers = {
            'Authorization': settings.POS_API_AUTH_HEADER
        }
        gift_claiming_points_api_url = '{}gift/claiming_points/'.format(
            settings.BASE_URL_POS_API)

        # Call POS get card member infomation
        response = requests.get(gift_claiming_points_api_url, headers=headers)

        if response.status_code == 401:
            print "POS reponse status code 401", response.text
            error = {"code": 500, "message": _(
                "Call API Unauthorized."), "fields": ""}
            return Response(error, status=500)
        if response.status_code != 200 and response.status_code != 400:
            print "POS reponse status code not 200", response.text
            error = {"code": 500, "message": _(
                "Call API error."), "fields": ""}
            return Response(error, status=500)

        # Get data from pos api reponse
        result = response.json()

        # Translate error message when code is 400
        if response.status_code == 400:
            result["message"] = _(result["message"])
            return Response(result, status=response.status_code)

        # Call success
        return Response(result, status=200)

    except requests.Timeout:
        print "Request POS time out "
        error = {"code": 500, "message": _(
                "API connection timeout."), "fields": ""}
        return Response(error, status=500)

    except Exception, e:
        print('get_gift_claiming_points: %s', traceback.format_exc())
        error = {"code": 500, "message": "%s" % e, "fields": ""}
        return Response(error, status=500)



"""
    Get Card member information
"""


@api_view(['POST'])
def card_member_link(request):
    print "Card member link"
    try:
        """
            1. Check user linked
            2. Check card member exist in request
            3. Get pos data by card member
            4. Check phone is match  
        """
        card_member = request.data.get('card_member', '')
        if not card_member:
            error = {"code": 400, "message": _(
                "Card member is required."), "fields": "card_member"}
            return Response(error, status=400)

        user = request.user
        linkcard = LinkCard.objects.filter(Q(user=user) | Q(card_member=card_member))
        if linkcard:
            error = {"code": 400, "message": _(
                "User or Card member have linked."), "fields": ""}
            return Response(error, status=400)

        # Call action get data response
        responses = actions.get_card_member_infomation_data(card_member)
    
        if responses["status"] != 200:
            # Return data with json
            return JsonResponse(results, status=responses["status"])

        results = responses['results']

        if not results:
            error = {"code": 400, "message": _("Card member not found."), "fields": ""}
            return Response(error, status=400)

        if not results['phone'] and not user.phone:
            error = {"code": 400, "message": _("Invalid Value."), "fields": ""}
            return Response(error, status=400)

        if results['phone'][1:] ==  user.phone:
            linkcard = LinkCard()
            linkcard.user = user
            linkcard.card_member = card_member
            linkcard.save()

            user.full_name = results['name'] if results['name'] else user.full_name
            user.birth_date = parse(results['birthday']) if results['birthday'] else user.birth_date
            user.personal_id = results['personal_id'] if results['personal_id'] else user.personal_id
            user.save()
            return Response(results, status=200)
        
        error = {"code": 400, "message": _("Phone not match."), "fields": ""}
        return Response(error, status=400)

    except Exception, e:
        print('card_member_link: %s', traceback.format_exc())
        error = {"code": 500, "message": "%s" % e, "fields": ""}
        return Response(error, status=500)
