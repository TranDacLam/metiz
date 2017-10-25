from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from booking.models import MovieSync
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
                    result[item["MOVIE_ID"]] = []

                # Check time showing greater than currnet hour
                if int(item["TIME"].split(':')[0]) >= current_date.hour:
                    result[item["MOVIE_ID"]].append(item["TIME"])

        return JsonResponse(result)

    except Exception, e:
        print "Error get_movie_show_time : %s" % e
        return HttpResponse(status=500)
