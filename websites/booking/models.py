from __future__ import unicode_literals

from django.db import models
from core.models import DateTimeModel
from django.utils.translation import ugettext_lazy as _


class BookingInfomation(DateTimeModel):
    TYPE = (
        ('cancel', 'Cancel'),
        ('confirm_error', 'Confirm Error'),
        ('payment_error', 'Payment Error'),
        ('pendding', 'Pendding'),
        ('done', 'Done')
        
    )
    GATE_TYPE = (
        ('VNPay', 'VNPay'),
        ('Helio_Payment_Card', 'Helio Payment Card'),
        ('Metiz_Payment_Card', 'Metiz Payment Card'),
    )
    user = models.ForeignKey(
        "core.User", related_name='user_booking_rel', null=True, blank=True)
    # movie = models.ForeignKey("core.Movie", related_name='movie_booking_rel')
    order_id = models.CharField(_('Order ID'), max_length=100)
    amount = models.FloatField(_('Amount'))
    phone = models.CharField(_('Phone'), null=True, blank=True, max_length=255)
    email = models.CharField(_('Email'), max_length=100, null=True, blank=True)
    seats = models.TextField(_('Seats'))
    barcode = models.CharField(max_length=100, null=True, blank=True)
    order_desc = models.TextField(_("Description"))
    id_server = models.IntegerField(default=1)
    order_status = models.CharField(max_length=50, choices=TYPE, default="pendding")
    barcode_confirm = models.CharField(max_length=100, null=True, blank=True)
    desc_transaction = models.CharField(max_length=500, null=True, blank=True)
    retry_ipn = models.IntegerField(default=0)
    poster = models.CharField(max_length=500, null=True, blank=True)
    gate_payment = models.CharField(_('Gate Payment'), choices=GATE_TYPE, max_length=500, null=True, blank=True)
    card_barcode = models.CharField(_('Card Barcode'), max_length=500, null=True, blank=True)

class MovieSync(DateTimeModel):
    TYPE = (
        ('movie_comming', 'Movie Comming Soon'),
        ('movie_showing', 'Movie Showing'),
        ('showtime_current', 'Show Times'),
    )
    name = models.CharField(max_length=50, choices=TYPE)
    # cinema_id is equal id_server
    cinema_id = models.IntegerField(default=1)
    area_id = models.IntegerField(default=0)
    data = models.TextField()
    date_show = models.DateField(_("Date Showing"))

    def __str__(self):
        return '%s' % (self.name)