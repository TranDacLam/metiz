# -*- coding: utf-8 -*-
from django import template
from datetime import timedelta
from django.utils import timezone
from core.models import Movie, Rated
from booking.models import MovieSync
import json
register = template.Library()


@register.filter
def floatdot(value, decimal_pos=4):
    return format(value, '.%if' % decimal_pos)


floatdot.is_safe = True


@register.simple_tag
def get_movie_name(movie_id):
    try:
        m = Movie.objects.get(movie_api_id=movie_id)
        return m.name
    except Movie.DoesNotExist, e:
        return None
    except Exception, e:
        return None


@register.simple_tag
def verify_showtime_by_id(cinema_id, movie_api_id):
    try:
        """
            Get all movie sync with condition date show greater than or equal to current date
            Check data movie contain movie_api_id 
        """
        result = False

        data_movie = MovieSync.objects.filter(
            name="showtime_current", date_show__gte=timezone.localtime(timezone.now()).date(), cinema_id=1)
        
        if data_movie:
            for item in data_movie:
                if item.data.find(movie_api_id) > -1:
                    result = True
                    break
        return result
    except Exception, e:
        return False


@register.simple_tag
def get_date_showing():
    current_date = timezone.localtime(timezone.now()).date()
    end_date = current_date + timedelta(days=6)
    step_date = timedelta(days=1)

    result = []
    while current_date <= end_date:
        result.append(current_date)
        current_date = current_date + step_date
    return result


@register.simple_tag
def get_cites():
    return {"data": ["Đà Nẵng"]}


@register.simple_tag
def get_cinema_cites():
    return ["Metiz Cinema"]


@register.simple_tag
def get_rated():
    rated = Rated.objects.values('name', 'description')
    data = {item['name'] : item['description'] for item in rated }
    return json.dumps(data)