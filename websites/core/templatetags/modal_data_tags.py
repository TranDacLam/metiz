from django import template
from datetime import date, timedelta
from django.http import JsonResponse
from django.utils import timezone
from booking.models import MovieSync
import json
import ast

register = template.Library()
@register.filter(name='get_data_modal')
def get_data_modal(date, cinema_id=1):
    try:
    	date = "2017-10-18"
        if not cinema_id:
            cinema_id = 1

        data_show_time = {}
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
                return {}

            # Generate dictionary result key is movie_id and values is time
            # showing
            for item in show_times["List"]:
                # Check key not in result then create dictionary create new key
                # with data is list empty
                if item["MOVIE_ID"] not in data_show_time:
                    data_show_time[item["MOVIE_ID"]] = {"times": [], "id_showtime": item[
                        "ID"], "movie_id": item["MOVIE_ID"]}

                # Check time showing greater than currnet hour
                current_date = timezone.localtime(timezone.now())
                if int(item["TIME"].split(':')[0]) >= current_date.hour:
                    data_show_time[item["MOVIE_ID"]]["times"].append(item["TIME"])

        data_cinema = {
            'danang': {"id_area": 1, "cinemas": {"id_server": 1, "name": "Metiz Cinema"}},
        }
    except Exception , e:
        print "Template Tag Get Show Times Errors ", e
        return {}
    return {'data_show_time': data_show_time, 'data_cinema': data_cinema}


@register.filter
def floatdot(value, decimal_pos=4):
    return format(value, '.%if'%decimal_pos)


floatdot.is_safe = True


@register.filter
def get_date_showing(data):
    print "Debug"
    current_date = date(2017, 10, 12)
    end_date = current_date + timedelta(days=6)
    step_date = timedelta(days=1)

    result = []
    while current_date <= end_date:
        result.append(current_date.strftime('%Y-%m-%d'))
        current_date = current_date + step_date
    print "get_date_showing",result
    return result
