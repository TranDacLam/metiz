from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from api import views
# from django.contrib import admin

urlpatterns = [
    url(r'^accounts/login/$', obtain_jwt_token, name="accounts-login"),
    url(r'^report/get_booking_info/$', views.get_booking_info_report, name='get-booking-info-report'),
    
    url(r'^card_member/link/$', views.card_member_link, name='card-member-link'),
    url(r'^gift/claiming_points/$', views.get_gift_claiming_points, name="get-gift-claiming-points"),
    url(r'^verify/card/member/$', views.verify_card_member, name="verify-card-member"),

]
