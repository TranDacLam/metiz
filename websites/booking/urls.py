from django.conf.urls import include, url
import views


urlpatterns = [
	url(r'^booking/$', views.get_booking, name='booking'),
    url(r'^movie/show/times$', views.get_movie_show_time, name='movie-show-time-by-date'),
    url(r'^movie/seats$', views.get_seats, name='movie-seats'),
    url(r'^verify/seats$', views.check_seats, name='verify-seats'),
    # url(r'^clear/seats$', views.clear_seats, name='clear-seats'),
    url(r'^timeout/$', views.time_out, name='time-out'),
    url(r'^invalid/booking/$', views.invalid_booking, name='invalid-booking'),
    url(r'^movie/api/ids/$', views.get_movie_api_ids, name='get_movie_api_ids'),
    
    # url(r'^movies/synchronize/$', views.movies_synchronize, name='movies-synchronize'),
]