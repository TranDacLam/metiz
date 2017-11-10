# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from booking.models import MovieSync
from booking.forms import BookingForm
from booking import api
import json
import ast
from datetime import timedelta
from core.models import Movie


def get_booking(request):
    try:
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
                id_sever = form.cleaned_data['id_sever']
                id_movie_name = form.cleaned_data['id_movie_name']
                id_movie_time = form.cleaned_data['id_movie_time']
                id_movie_date_active = form.cleaned_data[
                    'id_movie_date_active']
                print('*******booking******')
                return render(request, 'websites/booking.html', {"id_showtime": id_showtime, "id_sever": id_sever,
                                                                 "id_movie_name": id_movie_name, "id_movie_time": id_movie_time,
                                                                 "id_movie_date_active": id_movie_date_active})
            else:
                return render(request, 'websites/booking.html')
        else:
            print('*******booking******')
            id_showtime = request.GET.get('id_showtime', "")
            id_sever = request.GET.get('id_sever', 1)
            id_movie_name = request.GET.get('id_movie_name', "")
            id_movie_time = request.GET.get('id_movie_time', "")
            id_movie_date_active = request.GET.get('id_movie_date_active', "")
            return render(request, 'websites/booking.html', {"id_showtime": id_showtime, "id_sever": id_sever,
                                                             "id_movie_name": id_movie_name, "id_movie_time": id_movie_time,
                                                             "id_movie_date_active": id_movie_date_active})
    except Exception, e:
        print "Error get_booking : ", e
        return HttpResponse(status=500)


def time_out_booking(request):
    try:
        return render(request, 'websites/time_out_booking.html')
    except Exception, e:
        print "Error time out booking : ", e
        return HttpResponse(status=500)



def build_show_time_json(current_date, item, result, movies_info, obj_movie=None):    
    """ Build Data Json For Movie ShowTime """
                
    # Check key not in result then create dictionary create new key
    # with data is list empty
    if item["MOVIE_ID"] not in result:
        # GET movie object by movie_api_id detail or get by MOVIE_ID
        if not obj_movie:
            obj_movie = movies_info.filter(
                                movie_api_id=item["MOVIE_ID"])

        result[item["MOVIE_ID"]] = {"lst_times": [], "movie_id": item[
            "MOVIE_ID"], "movie_name": obj_movie[0].name if obj_movie else item["MOVIE_NAME_VN"],
            "rated": obj_movie[0].rated.name if obj_movie else None , "time_running": obj_movie[0].time_running if obj_movie else 0}

    # Check time showing greater than currnet hour
    if item["DATE"] == current_date.strftime("%d/%m/%Y"):
        if int(item["TIME"].split(':')[0]) >= current_date.hour:
            result[item["MOVIE_ID"]]["lst_times"].append(
                {"id_showtime": item["ID"], "time": item["TIME"]})
    else:
        result[item["MOVIE_ID"]]["lst_times"].append(
            {"id_showtime": item["ID"], "time": item["TIME"]})

def get_movie_show_time(request):
    try:
        """
            Get movie show times by date
        """
        current_date = timezone.localtime(timezone.now())

        date = request.GET.get('date', current_date.date())
        cinema_id = request.GET.get('cinema_id', 1)
        movie_api_id = request.GET.get('movie_api_id', None)

        result = {}
        data_movie = MovieSync.objects.filter(
            name="showtime_current", date_show=date, cinema_id=cinema_id)

        """ Check query set and get first item """
        if data_movie:
            # Validate convert data to json
            try:
                show_string = json.loads(data_movie[0].data)
                show_times = ast.literal_eval(show_string)

                # get all movies
                movies_info = Movie.objects.filter(
                    release_date__lte=date, end_date__gte=date)
            except ValueError as e:
                print "Error get_movie_show_time convert json : %s" % e
                return JsonResponse({})

            # Generate dictionary result key is movie_id and values is time
            # showing
            # get movie object if movie_api_id not empty
            obj_movie = None
            if movie_api_id:
                obj_movie = movies_info.filter(movie_api_id=movie_api_id)

            for item in show_times["List"]:
                # Get Showtime movie by id
                if movie_api_id:
                    # Get Movie Name by movie api id
                    if item["MOVIE_ID"] == movie_api_id:
                        build_show_time_json(current_date, item, result, movies_info, obj_movie)
                else:
                    build_show_time_json(current_date, item, result, movies_info)

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

            if data_seats and data_seats["List"] and seats_choice:
                seat_has_selected = []
                # check chairs of a user have been selected before
                for item in seats_choice:
                    chair = [str(s["NAME"]) for s in data_seats["List"] if s[
                        "ID"] == item["ID"] and s["STATUS"] == "True"]
                    if chair:
                        seat_has_selected.append(chair[0])

                if seat_has_selected:
                    return JsonResponse({"code": 400, "message": _("These chairs have been selected : %s" % seat_has_selected)}, status=400)
                else:
                    # Call Booking Seats
                    full_name = request.session.get("full_name", "")
                    phone = request.session.get("phone", "")
                    email = request.session.get("email", "")
                    # Get Information of user and building data for api update
                    # status of seats

                    result = api.call_api_post_booking(
                        full_name, phone, email, seats_choice, id_server, url="/postBooking")

                    if not result["BARCODE"]:
                        print "result ", result
                        return JsonResponse({"code": 400, "message": _("Cannot Booking Seats. Please Contact Administrator.")}, status=400)

                    # Add Seats into session and set seats expire in five
                    # minute
                    current_store = request.session.get("movies", {})
                    working_id = request.POST["working_id"]
                    if working_id in current_store:
                        """ 
                            If session exist id_showtime then append new seat item into session: 
                            Algorithm :
                             - step 1 : Cancel seats old in workingid and add new seats choice
                        """
                        if current_store[working_id]["seats_choice"]:
                            for seat_id in current_store[working_id]["seats_choice"]:
                                api.call_api_cancel_seat(
                                    seat_id=seat_id, id_server=id_server)

                        current_store[working_id][
                            "seats_choice"] = seats_choice
                        current_store[working_id]["time_choice"] = timezone.localtime(timezone.now(
                        ) + timedelta(minutes=settings.TIME_SEAT_DELAY)).strftime("%Y-%m-%d %H:%M:%S.%f"),

                    else:
                        # Add new id_showtime in store movie session
                        current_store[working_id] = {
                            "time_choice": timezone.localtime(timezone.now() + timedelta(minutes=settings.TIME_SEAT_DELAY)).strftime("%Y-%m-%d %H:%M:%S.%f"),
                            "seats_choice": seats_choice,
                            "id_showtime": id_showtime
                        }
                    print "### data_store ", current_store
                    request.session['movies'] = current_store

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


def clear_seeats(request):
    try:
        if request.method == "POST":
            if "working_id" not in request.POST:
                return JsonResponse({"code": 400, "message": _("Fields working_id is required.")}, status=400)

            id_server = request.POST.get("id_server", 1)
            working_id = request.POST["working_id"]
            movie_store = request.session.get("movies", {})
            # Check Working id exist in session and remove it
            if movie_store and working_id in movie_store:
                for seat_id in movie_store[working_id]["seats_choice"]:
                    print "##### Clear Seat ", seat_id
                    api.call_api_cancel_seat(
                        seat_id=seat_id["ID"], id_server=id_server)
                del movie_store[working_id]

                if movie_store:
                    request.session["movies"] = movie_store
                else:
                    del request.session["movies"]
            return JsonResponse({"result": True})
    except Exception, e:
        print "Error clear_seeats : %s ", e
        pass

