# -*- coding: utf-8 -*-
from django import template
from datetime import timedelta
from django.utils import timezone
from core.models import Movie

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
def get_date_showing():
    current_date = timezone.localtime(timezone.now()).date()
    end_date = current_date + timedelta(days=6)
    step_date = timedelta(days=1)

    result = []
    while current_date <= end_date:
        result.append(current_date.strftime('%Y-%m-%d'))
        current_date = current_date + step_date
    return result


@register.simple_tag
def get_cites():
    return {"data": ["Đà Nẵng"]}


@register.simple_tag
def get_cinema_cites():
    return ["Metiz Cinema"]
