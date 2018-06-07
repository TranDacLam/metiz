from django.shortcuts import render
from booking.models import BookingInfomation
from datetime import timedelta, datetime, time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponse
import serializers
import json
from rest_framework.decorators import api_view
from api import actions
# Create your views here.
import traceback


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


@api_view(['GET'])
def get_card_member_infomation(request):
    print "Get Card member information"
    try:
        headers = {
            'Authorization': settings.POS_API_AUTH_HEADER
        }
        gift_claiming_points_api_url = '{}card_member/information/'.format(
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
        print('get_card_member_infomation: %s', traceback.format_exc())
        error = {"code": 500, "message": "%s" % e, "fields": ""}
        return Response(error, status=500)

