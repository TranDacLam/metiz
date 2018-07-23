from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from api_app import views

urlpatterns = [
    url(r'^payment/booking/$', views.payment_booking, name="app-payment-booking"),
    url(r'^payment/methods/$', views.payment_method, name="app-payment-method"),
    url(r'^verify/card/payment/$', views.verify_payment_card, name="app-verify-payment-card"),
    url(r'^forgot/password/$', views.forgot_password, name="app-forgot-password"),
    url(r'^verify/otp/$', views.verify_otp, name="app-verify-otp"),
    url(r'^resend/otp/$', views.resend_otp, name="app-resend-otp"),
    
]
