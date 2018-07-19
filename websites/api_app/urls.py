from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from api_app import views

urlpatterns = [
    url(r'^movie/seats$', views.get_movie_seat, name="movie-seat"),
    url(r'^check/seats/$', views.check_movie_seat, name="check-seat"),

]
