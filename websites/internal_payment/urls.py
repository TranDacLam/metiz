"""vnpay_payment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^payment/method/$', views.metiz_payment_methods, name='metiz-payment-methods'),
    url(r'^invalid/payment$', views.invalid_payment, name='invalid-payment'),
    url(r'^payment/otp/$', views.generate_otp, name='payment-generate-otp'),
    url(r'^payment/otp/verify/$', views.verify_otp_for_user, name='payment-verify-otp'),
    
    # url(r'^payment_ipn$', views.payment_ipn, name='payment_ipn'),
    # url(r'^payment_return$', views.payment_return, name='payment_return'),
    # url(r'^query$', views.query, name='query'),
    # url(r'^refund$', views.refund, name='refund'),
]
