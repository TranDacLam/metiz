# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseNotAllowed
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from booking.models import BookingInfomation
from booking.forms import BookingForm
from booking import api
import json
import ast
from datetime import timedelta, datetime, time
from core.models import Movie

# Export to excel
import os
import xlsxwriter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
import os
from core.decorator import *
from django.core.management import call_command



@check_user_booking_exist
def get_booking(request):
    try:
        """ Action render page booking for user selected chair,
            this action support for two action get and post
        """
        if request.method not in ['POST', 'GET']:
            return HttpResponseNotAllowed(['POST', 'GET'])

        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                full_name = form.cleaned_data['name']
                phone = form.cleaned_data['phone']
                email = form.cleaned_data['email']
                request.session['full_name'] = full_name
                request.session['phone'] = phone
                request.session['email'] = email if email else None

                id_showtime = form.cleaned_data['id_showtime']
                id_server = form.cleaned_data['id_server']
                movie_api_id = form.cleaned_data['movie_api_id']
                id_movie_name = form.cleaned_data['id_movie_name']
                id_movie_time = form.cleaned_data['id_movie_time']
                id_movie_date_active = form.cleaned_data[
                    'id_movie_date_active']
                print('*******booking******')
                movie = Movie.objects.filter( movie_api_id = movie_api_id )
                poster = None
                if movie.count() == 1:
                    poster = movie.get().poster
                return render(request, 'websites/booking.html', {"id_showtime": id_showtime, "id_server": id_server,
                                                                 "id_movie_name": id_movie_name, "id_movie_time": id_movie_time,
                                                                 "id_movie_date_active": id_movie_date_active,
                                                                 "movie_api_id": movie_api_id,
                                                                 "poster": poster})
            else:
                return render(request, 'websites/booking.html')
        else:
            print('*******booking******')
            id_showtime = request.GET.get('id_showtime', "")
            id_server = request.GET.get('id_server', 1)
            movie_api_id = request.GET.get('movie_api_id', "")
            id_movie_name = request.GET.get('id_movie_name', "")
            id_movie_time = request.GET.get('id_movie_time', "")
            id_movie_date_active = request.GET.get('id_movie_date_active', "")
            movie = Movie.objects.filter( movie_api_id = movie_api_id )
            poster = None
            if movie.count() == 1:
                poster = movie.get().poster
            return render(request, 'websites/booking.html', {"id_showtime": id_showtime, "id_server": id_server,
                                                             "id_movie_name": id_movie_name, "id_movie_time": id_movie_time,
                                                             "id_movie_date_active": id_movie_date_active,
                                                             "movie_api_id": movie_api_id,
                                                             "poster": poster})
    except Exception, e:
        print "Error get_booking : ", e
        raise Exception(
            "ERROR : Internal Server Error .Please contact administrator.")


def time_out_booking(request):
    try:
        """ Action render page notification timeout for user """
        return render(request, 'websites/time_out_booking.html')
    except Exception, e:
        print "Error time out booking : ", e
        raise Exception(
            "ERROR : Internal Server Error .Please contact administrator.")

def invalid_booking(request):
    try:
        """ Action render page notification invalid money """
        return render(request, 'websites/invalid_money.html')
    except Exception, e:
        print "Error time out booking : ", e
        raise Exception(
            "ERROR : Internal Server Error .Please contact administrator.")


def build_show_time_json(current_date, item, result, movies_info, obj_movie=None):
    """ Build Data Json For Movie ShowTime """

    # Check key not in result then create dictionary create new key
    # with data is list empty
    if item["MOVIE_ID"] not in result:
        # GET movie object by movie_api_id detail or get by MOVIE_ID
        if not obj_movie:
            obj_movie = movies_info.filter(
                movie_api_id=item["MOVIE_ID"])

        # obj_movie[0].name.split(':')[0] to get vietnames film names
        result[item["MOVIE_ID"]] = {"lst_times": [], "movie_id": item[
            "MOVIE_ID"], "movie_name": obj_movie[0].name.split(':')[0] if obj_movie else item["MOVIE_NAME_VN"],
            "rated": obj_movie[0].rated.name if obj_movie and obj_movie[0].rated else None, "time_running": obj_movie[0].time_running if obj_movie else 0,
            "allow_booking": obj_movie[0].allow_booking if obj_movie else True
            }

    # Check time showing greater than currnet hour
    if item["DATE"] == current_date.strftime("%d/%m/%Y"):
        current_time = (current_date.hour) * 60 + current_date.minute
        time_show = (int(item["TIME"].split(':')[0])) * \
            60 + int(int(item["TIME"].split(':')[1]))
        # compare hour and minute
        if time_show >= current_time:
            result[item["MOVIE_ID"]]["lst_times"].append(
                {"id_showtime": item["ID"], "date": item["DATE"], 
                "time": item["TIME"], "room_name": item["ROOM_NAME"]})
    else:
        result[item["MOVIE_ID"]]["lst_times"].append(
            {"id_showtime": item["ID"], "date": item["DATE"], 
            "time": item["TIME"], "room_name": item["ROOM_NAME"]})


def get_movie_show_time(request):
    try:
        """
            Get movie show times by date
        """
        current_date = timezone.localtime(timezone.now())

        date = request.GET.get('date', current_date.date())
        # cinema_id is equal id_server
        cinema_id = request.GET.get('cinema_id', 1)
        movie_api_id = request.GET.get('movie_api_id', None)

        result = {}
        
        # call api to server king_pos get movie by date
        show_times = api.get_show_times(date)
        """ Check query set and get first item """
        if show_times:
            # Validate convert data to json
            try:
                # get all movies
                movies_info = Movie.objects.filter(Q(end_date__gte=date) | Q(end_date__isnull=True))
            except ValueError as e:
                print "Error get_movie_show_time convert json : %s" % e
                return JsonResponse({})

            # Generate dictionary result key is movie_id and values is time
            # showing
            # get movie object if movie_api_id not empty
            obj_movie = None
            if movie_api_id:
                obj_movie = movies_info.filter(
                    movie_api_id=movie_api_id.strip())

            for item in show_times["List"]:
                # Get Showtime movie by id
                if movie_api_id:
                    # Get Movie Name by movie api id
                    if item["MOVIE_ID"].strip() == movie_api_id.strip():
                        build_show_time_json(
                            current_date, item, result, movies_info, obj_movie)
                else:
                    build_show_time_json(
                        current_date, item, result, movies_info)

        return JsonResponse(result)

    except Exception, e:
        print "Error get_movie_show_time : %s" % e
        return JsonResponse({"code": 500, "message": _("Internal Server Error. Please contact administrator.")}, status=500)


def get_seats(request):
    try:
        """
            Get seats by show times id
        """
        result = {"List": []}
        id_server = request.GET.get('id_server', 1)

        if 'id_showtime' in request.GET:
            result = api.call_api_seats(request.GET["id_showtime"], id_server)
            return JsonResponse(result)
        else:
            error = {"code": 500, "message": _("Fields id_showtime and id_server is required."),
                     "fields": "id_showtime, id_server"}
            return JsonResponse(error, status=500)

    except Exception, e:
        print "Error get_seats : %s" % e
        return JsonResponse({"code": 500, "message": _("Internal Server Error. Please contact administrator.")}, status=500)


def check_seats(request):
    try:
        """
            Action verify seats have been selected before
            - step 1 : verify if seat aready selected then response error
            - step 2 : Seats no have selected then post booking for user
        """
        if request.method == "POST":
            # Validate Request Parameter id_server and lst_seats
            id_server = request.POST.get('id_server', 1)
            if "lst_seats" not in request.POST or "id_showtime" not in request.POST or 'working_id' not in request.POST:
                return JsonResponse({"code": 400, "message": _("Fields lst_seats and id_showtime, working_id is required.")}, status=400)

            # Get new seats from api
            id_showtime = request.POST["id_showtime"]
            data_seats = api.call_api_seats(
                id_showtime, id_server)
            # get list chair of user selected
            seats_choice = ast.literal_eval(request.POST["lst_seats"])

            total_money = 0

            if data_seats and data_seats["List"] and seats_choice:
                seat_has_selected = []
                # check chairs of a user have been selected before
                for item in seats_choice:
                    chair = [str(s["NAME"]) for s in data_seats["List"] if s[
                        "ID"] == item["ID"] and s["STATUS"] == "True"]

                    # Calculated total money
                    total_money += sum(int(s["PRICE"]) for s in data_seats["List"] if s[
                        "ID"] == item["ID"])

                    if chair:
                        seat_has_selected.append(chair[0])

                if seat_has_selected:
                    return JsonResponse({"code": 400, "message": _("These chairs have been selected : %s" % seat_has_selected)}, status=400)
                else:
                    print "********** Post Booking Get Barcode **********"
                    # init url api without member card
                    url = "/postBooking"
                    # Call Booking Seats
                    full_name = request.session.get("full_name", "")
                    phone = request.session.get("phone", "")
                    email = request.session.get("email", "")
                    # Get Information of user and building data for api update
                    # status of seats
                    member_card = request.POST.get('member_card')
                    # Change api url when card member is not null
                    if member_card:
                        url = "/postBookingMember"


                    result = api.call_api_post_booking(
                        full_name, phone, email, seats_choice, id_server, member_card, url)
                    
                    if not result["BARCODE"] or str(result["BARCODE"]) == '0' or total_money <= 0:
                        print "***** Get Barcode Fail : ", result
                        return JsonResponse({"code": 400, "message": _("Cannot Booking Seats. Please Contact Administrator.")}, status=400)

                    print "***** Information User Booking , Full Name: %s, Member Card: %s, Phone: %s, Email: %s, Barcode: %s, Money: %s"%(full_name, member_card, phone, email, result["BARCODE"], total_money)
                    # Add Seats into session and set seats expire in five
                    # minute
                    result["total_payment"] = total_money
                    current_store = request.session.get("movies", {})
                    working_id = request.POST["working_id"]
                    current_store[working_id] = {
                            "time_choice": timezone.localtime(timezone.now() + timedelta(minutes=settings.TIME_SEAT_DELAY)).strftime("%Y-%m-%d %H:%M:%S.%f"),
                            "seats_choice": seats_choice,
                            "barcode": result["BARCODE"],
                            "total_money": total_money
                        }
                    request.session['movies'] = current_store
                    
                    # current_store = request.session.get("movies", {})
                    # working_id = request.POST["working_id"]
                    # if working_id in current_store:
                    #     """
                    #         If session exist working_id then append new seat item into session:
                    #         Algorithm :
                    #          - Cancel seats old in workingid and add new seats choice
                    #     """
                    #     print "***** Working_id existing into sessions ", working_id
                    #     if current_store[working_id]["seats_choice"]:
                    #         for seat_id in current_store[working_id]["seats_choice"]:
                    #             print "***** Clear Old Seats of Working_id existing into sessions ", seat_id
                    #             api.call_api_cancel_seat(
                    #                 seat_id=seat_id, id_server=id_server)

                    #     print "***** Append New Seats for Working_id : ", seats_choice
                    #     current_store[working_id][
                    #         "seats_choice"] = seats_choice
                    #     current_store[working_id]["time_choice"] = timezone.localtime(timezone.now(
                    #     ) + timedelta(minutes=settings.TIME_SEAT_DELAY)).strftime("%Y-%m-%d %H:%M:%S.%f")

                    #     current_store[working_id]["total_money"] = total_money

                    # else:
                    #     # Add new key as working_id in store movie session
                    #     print "***** Add Working_id in Sessions : %s and list seats : %s  "%(working_id, seats_choice)
                    #     current_store[working_id] = {
                    #         "time_choice": timezone.localtime(timezone.now() + timedelta(minutes=settings.TIME_SEAT_DELAY)).strftime("%Y-%m-%d %H:%M:%S.%f"),
                    #         "seats_choice": seats_choice,
                    #         "barcode": result["BARCODE"],
                    #         "total_money": total_money
                    #     }
                    # print "***** Store Booking in Session, Phone: %s, Email: %s, Barcode: %s, Data Store: %s "%(phone, email, result["BARCODE"], current_store)
                    # request.session['movies'] = current_store

                    return JsonResponse(result)
    except Exception, e:
        print "Error booking_seats : %s" % e
        return JsonResponse({"code": 500, "message": _("Internal Server Error. Please contact administrator.")}, status=500)


def booking_payment(request):
    try:
        if request.method == "POST":
            # Validate Request Parameter id_server and lst_seats
            if "barcode" not in request.POST:
                return JsonResponse({"code": 400, "message": _("Fields barcode is required.")}, status=400)

            id_server = request.POST.get('id_server', 1)

            result_confirm = api.call_api_booking_confirm(
                request.POST["BARCODE"], id_server)

            return JsonResponse(result_confirm)

    except Exception, e:
        print "Error booking_payment : %s" % e
        return JsonResponse({"code": 500, "message": _("Internal Server Error. Please contact administrator.")}, status=500)


# def clear_seats(request):
#     try:
#         if request.method == "POST":
#             if "working_id" not in request.POST:
#                 return JsonResponse({"code": 400, "message": _("Fields working_id is required.")}, status=400)

#             id_server = request.POST.get("id_server", 1)
#             working_id = request.POST["working_id"]
#             movie_store = request.session.get("movies", {})
#             # Check Working id exist in session and remove it
#             if movie_store and working_id in movie_store:
#                 for seat_id in movie_store[working_id]["seats_choice"]:
#                     print "##### Clear Seat ", seat_id
#                     api.call_api_cancel_seat(
#                         seat_id=seat_id["ID"], id_server=id_server)
#                 del movie_store[working_id]

#                 if movie_store:
#                     request.session["movies"] = movie_store
#                 else:
#                     del request.session["movies"]
#             return JsonResponse({"result": True})
#     except Exception, e:
#         print "Error clear_seats : %s ", e
#         pass

@login_required(login_url='/admin/login/')
@permission_required('is_superuser', login_url='/admin/login/')
def movies_synchronize(request):
    try:
        if request.method == "POST":
            call_command("sync_movie")
            return JsonResponse({"message": "Success Synchronize movies."}, status=200)
        else:
            return render(request, 'websites/booking/movies_synchronize.html')
    except Exception, e:
        print "Error Action movies_synchronize : ",e
        return JsonResponse({"message": "Cannot synchronize movies. Please contact administrator "}, status=500)

def time_out_movie(request):
    try:
        """ Action render page notification timeout for user """
        return render(request, 'websites/time_out_movie.html')
    except Exception, e:
        print "Error time out movie : ", e
        raise Exception(
            "ERROR : Internal Server Error .Please contact administrator.")
