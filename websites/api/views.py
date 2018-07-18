from django.shortcuts import render
from booking.models import BookingInfomation
from datetime import timedelta, datetime, time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
import serializers
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from api import actions
# Create your views here.
import traceback
import requests
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from core.models import *
from dateutil.parser import parse
from rest_framework.views import exception_handler, APIView

def custom_exception_handler(exc, context):
    # to get the standard error response.
    response = exception_handler(exc, context)
    # Now add the HTTP status code to the response.
    if response is not None:
        try:
            message = exc.detail.values()[0][0] if exc.detail else ""
            field = exc.detail.keys()[0] if exc.detail else ""
        except Exception, e:
            print "custom_exception_handler ", e
            message = "errors"
            field = ""

        response.data['code'] = response.status_code
        response.data['message'] = response.data[
            'detail'] if 'detail' in response.data else str(message)
        response.data['fields'] = field
        if 'detail' in response.data:
            del response.data['detail']

    return response

@api_view(['GET'])
def get_booking_info_report(request):
    print "Get booking online Data"
    try:
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
        return Response(responses['results'], status=responses["status"])

    except Exception, e:
        print "Error booking_info_report : %s ", traceback.format_exc()
        error = {"code": 500, "message": "ERROR : Internal Server Error .Please contact administrator.", "fields": ""}
        return Response(error, status=500)

"""
    Get gift claiming points
"""


@api_view(['GET'])
def get_gift_claiming_points(request):
    print "Get gift claiming points"
    try:
        responses = actions.get_gift_claiming_points_data()
        if responses['code'] != 200:
            # Return data with json
            return Response(responses, status=responses["code"])

        result = responses['data']
        return Response(result, status=200)

    except Exception, e:
        print('get_gift_claiming_points: %s', traceback.format_exc())
        error = {"code": 500, "message": "ERROR : Internal Server Error .Please contact administrator.", "fields": ""}
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

        linkcard = LinkCard.objects.filter(card_member=card_member)
        if linkcard:
            error = {"code": 400, "message": _(
                "Card member have linked."), "fields": ""}
            return Response(error, status=400)

        user = request.user
        linkcard = LinkCard.objects.filter(user=user)
        if linkcard:
            error = {"code": 400, "message": _(
                "User have linked."), "fields": ""}
            return Response(error, status=400)

        # Call action get data response
        responses = actions.get_card_member_infomation_data(card_member)
    
        if responses["code"] != 200:
            # Return data with json
            return Response(responses, status=responses["code"])

        results = responses['data']
        if not results:
            error = {"code": 400, "message": _("Card member not found."), "fields": ""}
            return Response(error, status=400)

        if not results['phone'] and not user.phone:
            error = {"code": 400, "message": _("Invalid Value."), "fields": ""}
            return Response(error, status=400)
        print results['phone'][1:]
        if results['phone'][1:] ==  user.phone:
            linkcard = LinkCard()
            linkcard.user = user
            linkcard.card_member = card_member
            linkcard.save()

            user.full_name = results['name'] if results['name'] else user.full_name
            user.birth_date = parse(results['birthday']) if results['birthday'] else user.birth_date
            user.personal_id = results['personal_id'] if results['personal_id'] else user.personal_id
            user.save()
            results['card_member'] = card_member
            return Response(results, status=200)
        
        error = {"code": 400, "message": _("Phone not match."), "fields": ""}
        return Response(error, status=400)

    except Exception, e:
        print('card_member_link: %s', traceback.format_exc())
        error = {"code": 500, "message": "ERROR : Internal Server Error .Please contact administrator.", "fields": ""}
        return Response(error, status=500)


"""
    Verify Card member
"""


@api_view(['POST'])
@permission_classes((AllowAny,))
def verify_card_member(request):
    print "Verify Card member"
    try:
        """
            1. Call api pos dmz verify card member using for point bonus
        """
        card_member = request.data.get('card_member', '')
        if not card_member:
            error = {"code": 400, "message": _(
                "Card member is required."), "fields": "card_member"}
            return Response(error, status=400)
        
        # Call action get data response
        responses = actions.verify_card_member_pos(card_member)

        if responses["code"] != 200:
            # Return data with json
            return Response(responses, status=responses["code"])

        results = responses['data']
        return Response(results, status=200)

    except Exception, e:
        print('card_member_link: %s', traceback.format_exc())
        error = {"code": 500, "message": "ERROR : Internal Server Error .Please contact administrator.", "fields": ""}
        return Response(error, status=500)
