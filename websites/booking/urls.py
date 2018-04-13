from django.conf.urls import include, url
import views


urlpatterns = [
	url(r'^booking/$', views.get_booking, name='booking'),
    url(r'^movie/show/times$', views.get_movie_show_time, name='movie-show-time-by-date'),
    url(r'^movie/seats$', views.get_seats, name='movie-seats'),
    url(r'^verify/seats$', views.check_seats, name='verify-seats'),
    url(r'^clear/seats$', views.clear_seats, name='clear-seats'),
    url(r'^timeout/booking$', views.time_out_booking, name='time-out-booking'),
    url(r'^invalid/booking$', views.invalid_booking, name='invalid-booking'),
    url(r'^movies/synchronize/$', views.movies_synchronize, name='movies-synchronize'),
]