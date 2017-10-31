from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone
from booking import api


class DestroySeat(MiddlewareMixin):

    def process_request(self, request):
        try:
            movies = request.session.get("movies", "")
            if movies:
                
                print "movies session ", movies
                current_time = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S.%f")
                print "current_time ",current_time
                for key, value in movies.items():
                    print "##### TIME SET ",value["time_choice"]
                    print 
                    # Compare end time expired
                    if value["time_choice"] < current_time:
                        seats_choice = value["seats_choice"]
                        print "Destroy Seats middleware ", seats_choice
                        for seat in seats_choice:
                            api.call_api_cancel_seat(seat["ID"])

                        del movies[key]
                print "After Destroy Seat ", movies
                if movies:
                    request.session["movies"] = movies
                else:
                    del request.session["movies"]
        except Exception, e:
            print "Error process_request ", e
            pass
