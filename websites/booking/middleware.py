from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from booking import api


class DestroySeat(object):

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_request(self, request):
        try:
            time_choice = request.session.get("time_choice", "")
            if time_choice and time_choice + timedelta(minutes=settings.TIME_SEAT_DELAY) < timezone.localtime(timezone.now()):
                seats_choice = request.session.get("seats_choice", [])
                print "Destroy Seats middleware ", seats_choice
                for item in seats_choice:
                    api.call_api_cancel_seat(item["ID"])

                del request.session["time_choice"]
                del request.session["seats_choice"]
        except Exception, e:
            pass
