from django.conf.urls import include, url
import views


urlpatterns = [
    url(r'^movie/show/times$', views.get_movie_show_time, name='movie-show-time-by-date'),
]