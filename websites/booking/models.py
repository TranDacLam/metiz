from __future__ import unicode_literals

from django.db import models
from core.models import DateTimeModel
from django.utils.translation import ugettext_lazy as _


class BookingInfomation(DateTimeModel):
    TYPE = (
        ('cancel', 'Cancel'),
        ('pendding', 'Pendding'),
        ('done', 'Done')
    )
    user = models.ForeignKey(
        "core.User", related_name='user_booking_rel', null=True, blank=True)
    # movie = models.ForeignKey("core.Movie", related_name='movie_booking_rel')
    order_id = models.CharField(_('Order ID'), max_length=100)
    amount = models.FloatField(_('Amount'))
    phone = models.IntegerField(_('Phone'), null=True, blank=True)
    email = models.CharField(_('Email'), max_length=100, null=True, blank=True)
    seats = models.TextField(_('Seats'))
    barcode = models.CharField(max_length=100, null=True, blank=True)
    order_desc = models.TextField(_("Description"))
    id_server = models.IntegerField(default=1)
    order_status = models.CharField(max_length=50, choices=TYPE, default="pendding")
    barcode_confirm = models.CharField(max_length=100, null=True, blank=True)

class MovieSync(DateTimeModel):
    TYPE = (
        ('movie_comming', 'Movie Comming Soon'),
        ('movie_showing', 'Movie Showing'),
        ('showtime_current', 'Show Times'),
    )
    name = models.CharField(max_length=50, choices=TYPE)
    cinema_id = models.IntegerField(default=1)
    area_id = models.IntegerField(default=0)
    data = models.TextField()
    date_show = models.DateField(_("Date Showing"))

    def __str__(self):
        return '%s' % (self.name)