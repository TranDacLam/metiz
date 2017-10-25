
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from booking.models import MovieSync
import json
import ast
import urllib
import urllib2
import requests


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
                    result[item["MOVIE_ID"]] = {"times": [], "id_showtime": item[
                        "ID"], "movie_id": item["MOVIE_ID"]}

                # Check time showing greater than currnet hour
                if int(item["TIME"].split(':')[0]) >= current_date.hour:
                    result[item["MOVIE_ID"]]["times"].append(item["TIME"])

        return JsonResponse(result)

    except Exception, e:
        print "Error get_movie_show_time : %s" % e
        return HttpResponse(status=500)


def get_seats(request):
    try:
        """
            Get seats by show times id
        """
        result = {"List": []}
        id_server = request.GET.get('id_server', 1)

        if 'id_showtime' in request.GET:
            url_show_time = settings.BASE_URL_CINESTAR + "/getSeats"
            values = {
                "id_ShowTimes": request.GET['id_showtime'],
                "id_Server": id_server,
                "Secret": settings.CINESTAR_SERECT_KEY
            }
            request = urllib2.Request(url_show_time, data=urllib.urlencode(values),
                                      headers={'Content-Type': 'application/x-www-form-urlencoded'})
            resp = urllib2.urlopen(request)
            # handle decoding json
            try:
                result = json.loads(resp.read())

            except ValueError as e:
                print "Error convert json : %s" % e
                return JsonResponse({"code": 500, "message": _("Handle data error.")}, status=500)

            return JsonResponse(result)
        else:
            error = {"code": 500, "message": _("Fields id_showtime and id_server is required."),
                     "fields": "id_showtime, id_server"}
            return JsonResponse(error, status=500)

    except Exception, e:
        print "Error get_seats : %s" % e
        return JsonResponse({"code": 500, "message": _("Internal Server Error. Please contact administrator.")}, status=500)
