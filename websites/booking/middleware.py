from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from booking import api


class DestroySeat:

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
