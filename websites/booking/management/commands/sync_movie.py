from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.conf import settings
import json
import urllib
import urllib2
import requests
from booking.models import MovieSync
from datetime import timedelta


class Command(BaseCommand):
    help = 'Synchronize movie with cinestar server'

    def get_show_times(self, current_date, id_movie=0, id_movie_theater=0, id_area=0, id_server=1):
        """ 
            Get Movie Show Times
            default data
            - id_movie is zero get all movie
            - id_movie_theater is zero get all movie_theater
            - id_area is zero get all area (danang, hanoi, hcm, etc)
            - id_server is one as cinema metiz at helio center (cenima_id)
        """
        url_show_time = settings.BASE_URL_CINESTAR + "/getShowTimes"
        values = {
            "id_Movie": id_movie,
            "id_MovieTheater": id_movie_theater,
            "id_Area": id_area,
            "id_Server": id_server,
            "Date": current_date,
            "Secret": settings.CINESTAR_SERECT_KEY
        }
        request = urllib2.Request(url_show_time, data=urllib.urlencode(values),
                                  headers={'Content-Type': 'application/x-www-form-urlencoded'})
        resp = urllib2.urlopen(request)
        # handle decoding json
        try:
            result_dic = json.dumps(resp.read())
            movie, created = MovieSync.objects.get_or_create(
                name="showtime_current", date_show=current_date, cinema_id=id_server, area_id=id_area)
            movie.data = result_dic
            movie.save()
        except ValueError as e:
            print "Error convert json : %s" % e
            pass

    # def get_movies(self, status=2, id_movie=0, id_movie_formats=0, id_movie_type=0, id_country=0, id_server=1, name="movie_showing"):
    #     """
    #         Get Movies
    #         default data
    #         - id_movie is zero get all movie
    #         - id_movie_formats is zero get all formats
    #         - id_movie_type is zero get all types
    #         - id_country is zero get all country production movie
    #         - id_server is one as cinema metiz at helio center (cenima_id)
    #         - Status: number zero is get all , number one is movie comming soon, number two is movie showing, number three is movie special
    #     """
    #     url_movie = settings.BASE_URL_CINESTAR + "/getMovie"
    #     values = {
    #         "id_Movie": id_movie,
    #         "id_MovieFormats": id_movie_formats,
    #         "id_MovieType": id_movie_type,
    #         "id_Country": id_country,
    #         "id_Server": id_server,
    #         "Status": status,
    #         "Secret": settings.CINESTAR_SERECT_KEY
    #     }
    #     request = urllib2.Request(url_movie, data=urllib.urlencode(values),
    #                               headers={'Content-Type': 'application/x-www-form-urlencoded'})
    #     resp = urllib2.urlopen(request)
    #     # handle decoding json
    #     try:
    #         result_dic = json.loads(resp.read())
    #         movie, created = MovieSync.objects.get_or_create(
    #             name=name, cinema_id=id_server)
    #         movie.data = result_dic
    #         movie.save()
    #         for item in result_dic["List"]:

    #     except ValueError as e:
    #         print "Error convert json : %s" % e
    #         pass

    def handle(self, *args, **options):
        """ 
            Sync Moive 
            - Get Current Date
            - Get Show Time by Date
            - Get Movie Comming Soon
            - Get Movie Showing
        """
        try:
            current_date = timezone.localtime(
                timezone.now())
            # current_date = datetime.date(2017, 10, 12)
            end_date = current_date + timedelta(days=6)
            step_date = timedelta(days=1)

            while current_date <= end_date:
                self.get_show_times(current_date=current_date.strftime('%Y-%m-%d'))
                current_date = current_date + step_date
            
        except Exception, e:
            print "Error synchronize movie : %s" % e
            pass
