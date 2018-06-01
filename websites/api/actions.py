from django.shortcuts import render
from booking.models import BookingInfomation
from datetime import timedelta, datetime, time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponse
import serializers
import json

# Create your views here.


def get_booking_info_data(user_id=None, page_items=0, page_number=1, order_status=None, order_id=None,
                          email=None, phone=None, barcode=None, date_from=None, date_to=None):
    print "Get booking online Data Action"
    # Init reponse with status 200 (success)

    try:
        data_response = {
            "status": 200,
            "safe": True
        }

        booking_info_list = BookingInfomation.objects.all().order_by('-created')

        kwargs = {}
        # If paramter is not null then append condition to query
        if user_id:
            kwargs['user_id'] = user_id
        if order_id:
            kwargs['order_id'] = order_id
        if order_status:
            kwargs['order_status__in'] = order_status
        if email:
            kwargs['email'] = email
        if phone:
            kwargs['phone'] = phone
        if barcode:
            kwargs['barcode'] = barcode
        if date_from:
            kwargs['created__gte'] = datetime.combine(
                datetime.strptime(date_from, "%d/%m/%Y").date(), time.min)
        if date_to:
            kwargs['created__lte'] = datetime.combine(
                datetime.strptime(date_to, "%d/%m/%Y").date(), time.max)
        if kwargs:
            booking_info_list = booking_info_list.filter(**kwargs)

        if page_items:
            # Get total items result
            total_items = len(booking_info_list)
            # Paginator
            paginator = Paginator(booking_info_list, page_items)

            try:
                page_data = paginator.page(page_number)
                result = {}
                result['data'] = serializers.BookingInfomationSerializer(
                    page_data, many=True).data
                result["recordsTotal"] = total_items
                result["recordsFiltered"] = total_items
                result["total_page"] = paginator.num_pages
                data_response["results"] = result

            except PageNotAnInteger:
                data_response["status"] = 400
                # If page is not an integer, deliver first page.
                data_response["results"] = {
                    "message": "Page Number Not Type Integer."}
            except EmptyPage:
                data_response["status"] = 400
                # If page is out of range (e.g. 9999), deliver last page of
                # results.
                data_response["results"] = {
                    "message": "Page Number Not Found."}
            # Return data if paging
            return data_response

        # Return all data
        data = serializers.BookingInfomationSerializer(
            booking_info_list, many=True).data

        data_response["safe"] = False
        data_response["results"] = data
        return data_response

    except Exception, e:
        print "Error booking_info_report : %s ", e
        raise Exception(
            "ERROR : Internal Server Error .Please contact administrator.")
