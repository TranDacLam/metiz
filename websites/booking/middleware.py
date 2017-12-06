from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone
from booking import api


class DestroySeat(MiddlewareMixin):

    def process_request(self, request):
        try:
            """ 
                Middleware call api cancel seats when session time out five minute
                step 1 : lookup in session of user check time_chooice(have add more five minute) less than current time then cancel seats
                step 2 : after cancel seat then remove key (working_id) into session
            """
            movies = request.session.get("movies", "")
            if movies:
                current_time = timezone.localtime(
                    timezone.now()).strftime("%Y-%m-%d %H:%M:%S.%f")
                for key, value in movies.items():
                    # Compare end time expired
                    if value["time_choice"] < current_time:
                        seats_choice = value["seats_choice"]
                        print "Destroy Seats middleware ", seats_choice
                        # lookup seats of key timeout and cancel it
                        for seat in seats_choice:
                            api.call_api_cancel_seat(seat["ID"])

                        # after remove seats then remove key into session
                        del movies[key]
                if movies:
                    # movie before check timeout if not empty then assign new movies for session
                    request.session["movies"] = movies
                else:
                    # delete session when empty
                    del request.session["movies"]
        except Exception, e:
            print "Error process_request ", e
            pass
