from django.shortcuts import render
from booking.models import BookingInfomation
from datetime import timedelta, datetime, time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponse
import serializers
import json
from rest_framework.decorators import api_view
# Create your views here.
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

        print order_status

        kwargs = {}
        # If paramter is not null then append condition to query
        if order_id:
            kwargs['order_id'] = order_id
        if order_status:
            print "test"
            kwargs['order_status__in'] = order_status
        if email:
            kwargs['email'] = email
        if phone:
            kwargs['phone'] = phone
        if barcode:
            kwargs['barcode'] = barcode
        if date_from:
            kwargs['created__gte'] = datetime.combine(datetime.strptime(date_from, "%d/%m/%Y").date(), time.min)
        if date_to:
            kwargs['created__lte'] = datetime.combine(datetime.strptime(date_to, "%d/%m/%Y").date(), time.max)
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
                result['data'] = serializers.BookingInfomationSerializer(page_data, many=True).data
                result["recordsTotal"] = total_items
                result["recordsFiltered"] = total_items
                return JsonResponse(result, status=200)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                return JsonResponse({"message": "Page Number Not Type Integer."}, status=400)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of
                # results.
                return JsonResponse({"message": "Page Number Not Found."}, status=400)

        data = serializers.BookingInfomationSerializer(booking_info_list, many=True).data

        return JsonResponse(data, safe=False, status=200)
    except Exception, e:
        print "Error booking_info_report : %s ", e
        raise Exception(
            "ERROR : Internal Server Error .Please contact administrator.")




