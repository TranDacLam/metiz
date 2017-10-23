from __future__ import unicode_literals

from django.db import models
from core.models import DateTimeModel
from django.utils.translation import ugettext_lazy as _


class BookingInfomation(DateTimeModel):
    user = models.ForeignKey(
        "core.User", related_name='user_booking_rel', null=True, blank=True)
    movie = models.ForeignKey("core.Movie", related_name='movie_booking_rel')
    order_id = models.CharField(_('Order ID'), max_length=100)
    amount = models.FloatField(_('Amount'))
    phone = models.IntegerField(_('Phone'), null=True, blank=True)
    email = models.CharField(_('Email'), max_length=100, null=True, blank=True)
