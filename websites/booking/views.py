from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from booking.models import MovieSync
from booking import api
import json
import ast



def get_movie_show_time(request):
    try:
        """
            Get movie show times by date
        """
        current_date = timezone.localtime(timezone.now())

        date = request.GET.get('date', current_date.date())
        cinema_id = request.GET.get('cinema_id', 1)

        result = {}
        data_movie = MovieSync.objects.filter(
            name="showtime_current", date_show=date, cinema_id=cinema_id)

        """ Check query set and get first item """
        if data_movie:
            # Validate convert data to json
            try:
                show_string = json.loads(data_movie[0].data)
                show_times = ast.literal_eval(show_string)

            except ValueError as e:
                print "Error get_movie_show_time convert json : %s" % e
                return JsonResponse({})

            # Generate dictionary result key is movie_id and values is time
            # showing
            for item in show_times["List"]:
                # Check key not in result then create dictionary create new key
                # with data is list empty
                if item["MOVIE_ID"] not in result:
                    result[item["MOVIE_ID"]] = {"lst_times": [], "movie_id": item[
                        "MOVIE_ID"], "movie_name": item["MOVIE_NAME_VN"]}

                # Check time showing greater than currnet hour
                if int(item["TIME"].split(':')[0]) >= current_date.hour:
                    result[item["MOVIE_ID"]]["lst_times"].append(
                        {"id_showtime": item["ID"], "time": item["TIME"]})

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
            if "lst_seats" not in request.POST or "id_showtime" not in request.POST:
                return JsonResponse({"code": 400, "message": _("Fields lst_seats and id_showtime is required.")}, status=400)

            # Get new seats from api
            data_seats = api.call_api_seats(request.POST["id_showtime"], id_server)
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

                    data_post_booking = {
                        "List": [
                            {
                                "NAME": full_name,
                                "PHONE": phone,
                                "EMAIL": email,
                                "ListSeats": seats_choice
                            }
                        ]
                    }
                    result = api.call_api_post_booking(
                        data_post_booking, id_server, url="/postBooking")

                    # Add Seats into session and set seats expire in five
                    # minute
                    request.session['time_choice'] = timezone.localtime(
                        timezone.now()).strftime('%Y-%m-%d')
                    request.session['seats_choice'] = seats_choice
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
