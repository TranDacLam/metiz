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
