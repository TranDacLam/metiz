from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from api import views
# from django.contrib import admin

urlpatterns = [
    url(r'^accounts/login/$', obtain_jwt_token, name="accounts-login"),
    url(r'^report/get_booking_info/$', views.get_booking_info_report, name='get-booking-info-report'),
]
