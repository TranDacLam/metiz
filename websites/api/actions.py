from django.shortcuts import render
from booking.models import BookingInfomation
from datetime import timedelta, datetime, time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponse
import serializers
import json
import requests
from django.conf import settings
import traceback
from django.utils.translation import ugettext_lazy as _

"""
    DMZ responde with:
    Case 1: 200 return data
    Case 2: 400 return data with message translate
    Else: Return erorr
"""
def code_mapping_error(status_code, json_data):
    print "json_data:::::::::"
    switcher = {
        200: json_data,
        401: {"code": 500, "message": _("Call API Unauthorized."), "fields": ""},
        400: {"code": 400, "message": _(json_data["message"]) if status_code==400 else json_data, "fields": ""}
    }
    return switcher.get(status_code, {"code": 500, "message": _("Call API error."), "fields": ""})


def get_booking_info_data(user_id=None, page_items=0, page_number=1, order_status=None, order_id=None,
                          email=None, phone=None, barcode=None, date_from=None, date_to=None):
    print "Get booking online Data Action"
    # Init reponse with status 200 (success)

    try:
        data_response = {
            "status": 200
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

        data_response["results"] = data
        return data_response

    except Exception, e:
        print "Error booking_info_report : %s ", e
        raise Exception(
            "ERROR : Internal Server Error .Please contact administrator.")

def get_card_member_infomation_data(card_member):
    print "Get Card member information data"
    data_response = {
        "status": 200
    }
    try:

        if not card_member:
            data_response["status"] = 400
            data_response["results"] = {"code": 400, "message": _("Card member is required."), "fields": "card_member"}
            return data_response

        params = {
            "card_member": card_member
        }
        # Add authorization to request header
        headers = {
            'Authorization': settings.POS_API_AUTH_HEADER
        }
        # Get link call api 
        gift_claiming_points_api_url = '{}card_member/information/'.format(
            settings.BASE_URL_POS_API)

        # Call POS get card member infomation
        response = requests.get(gift_claiming_points_api_url, params=params, headers=headers)


        try:
            # convert response text to json
            json_data = json.loads(response.text)
        except ValueError as e:
            print "Error convert json : %s" % e
            return {"code": 500, "message": _("Handle data error.")}

        # Mapping status dmz reponse with reponse
        result = code_mapping_error(response.status_code, json_data)
        if response.status_code != 200 :
            print "DMZ Response Text:::", response.text
            return result

        return {"code": 200, "data": result}

    except requests.Timeout:
        print "Request POS time out "
        return {"code": 500, "message": _("API connection timeout."), "fields": ""}

    except Exception, e:
        print('get_card_member_infomation: %s', traceback.format_exc())
        raise Exception(
            "ERROR : Internal Server Error .Please contact administrator.")


def verify_card_member_pos(card_member):
    data_response = {
        "status": 200
    }
    try:
        params = {
            "card_member": card_member
        }
        # Add authorization to request header
        headers = {
            'Content-type': 'application/json',
            'Authorization': settings.POS_API_AUTH_HEADER
        }
        # Get link call api 
        url_verify_card = '{}verify/card/member/'.format(
            settings.BASE_URL_POS_API)
        
        # Call POS get card member infomation
        response = requests.post(url_verify_card, data=json.dumps(params), headers=headers)
        try:
            # convert response text to json
            json_data = json.loads(response.text)
        except ValueError as e:
            print "Error convert json : %s" % e
            return {"code": 500, "message": _("Handle data error.")}

        # Mapping status dmz reponse with reponse
        result = code_mapping_error(response.status_code, json_data)
        if response.status_code != 200 :
            print "DMZ Response Text:::", response.text
            return result

        return {"code": 200, "data": result}

    except requests.Timeout:
        print "Request POS time out "
        return {"code": 500, "message": _("API connection timeout."), "fields": ""}
    except Exception, e:
        print('get_card_member_infomation: %s', traceback.format_exc())
        raise Exception(
            "ERROR : Internal Server Error .Please contact administrator.")

def get_gift_claiming_points_data():
    try:
        headers = {
            'Authorization': settings.POS_API_AUTH_HEADER
        }
        gift_claiming_points_api_url = '{}gift/claiming_points/'.format(
            settings.BASE_URL_POS_API)

        # Call POS get card member infomation
        response = requests.get(gift_claiming_points_api_url,  headers=headers)

        try:
            # convert response text to json
            json_data = json.loads(response.text)
        except ValueError as e:
            print "Error convert json : %s" % e
            return {"code": 500, "message": _("Handle data error.")}

        # Mapping status dmz reponse with reponse
        result = code_mapping_error(response.status_code, json_data)

        if response.status_code != 200 :
            print "DMZ Response Text:::", response.text
            return result

        return {"code": 200, "data": result}

    except requests.Timeout:
        print "Request POS time out "
        return {"code": 500, "message": _(
                "API connection timeout."), "fields": ""}

    except Exception, e:
        print('get_gift_claiming_points: %s', traceback.format_exc())
        return {"code": 500, "message": "ERROR : Internal Server Error .Please contact administrator.", "fields": ""}

