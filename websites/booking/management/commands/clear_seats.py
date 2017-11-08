from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.conf import settings
import json
import urllib
import urllib2
import requests
from booking.models import BookingInfomation
from datetime import timedelta
from booking import api


class Command(BaseCommand):
    help = 'Clear Seats Order Pending'

    def cancel_seat(self, lst_seats, id_server=1):
        """ 
            Call Api Cancel Seat
            - id_server is one as cinema metiz at helio center (cenima_id)
        """
        try:
            for seat in lst_seats:
                api.call_api_cancel_seat(seat, id_server)
        except Exception as e:
            print "Error Call Api Cancel Seat : %s" % e
            pass

    def handle(self, *args, **options):
        """ 
            Clear Seats
            - Get Booking with order status pendding
            - Check order timeout teen minute
            - Call Api Cancel seat
            - Remove order
        """
        try:
            print "Handle clear seat every 5 minute"
            bookings = BookingInfomation.objects.filter(order_status='pendding')
            if bookings:
                current_time = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S.%f")
                for item in bookings:
                    if (timezone.localtime(item.created) + timedelta(minutes=6)).strftime("%Y-%m-%d %H:%M:%S.%f") < current_time:
                        self.cancel_seat(item.seats.split(','), item.id_server)
                        item.order_status = 'cancel'
                        item.save()
        except Exception, e:
            print "Error synchronize movie : %s" % e
            pass
