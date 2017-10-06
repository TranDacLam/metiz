"""helio_web URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
import views
from django.conf import settings
from django.conf.urls.static import static


handler404 = 'main.views.custom_404'
handler500 = 'main.views.custom_500'

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^', include('registration.urls')),
    
    
    url(r'^cinox/$', views.cinox, name='cinox'),
    url(r'^cinox_detail/$', views.cinox_detail, name='cinox_detail'),
    url(r'^gift_card/$', views.gift_card, name='gift_card'),
    url(r'^membership/$', views.membership, name='membership'),
    url(r'^account_create/$', views.account_create, name='account_create'),
    url(r'^account_login/$', views.account_login, name='account_login'),
    url(r'^account_findmember/$', views.account_findmember, name='account_findmember'),
    url(r'^account_forgot_password/$', views.account_forgot_password, name='account_forgot_password'),
    url(r'^arthouse/$', views.arthouse, name='arthouse'),
    url(r'^movie_voucher/$', views.movie_voucher, name='movie_voucher'),
    url(r'^about_cinema/$', views.about_cinema, name='about_cinema'),
    url(r'^gift_card_detail/$', views.gift_card_detail, name='gift_card_detail'),
    url(r'^gift_card_online_detail/$', views.gift_card_online_detail, name='gift_card_online_detail'),
    url(r'^cgv_online/$', views.cgv_online, name='cgv_online'),
    url(r'^careers/$', views.careers, name='careers'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^terms_conditions/$', views.terms_conditions, name='terms_conditions'),
    url(r'^terms_use/$', views.terms_use, name='terms_use'),
    url(r'^payment_policy/$', views.payment_policy, name='payment_policy'),
    url(r'^privacy_policy/$', views.privacy_policy, name='privacy_policy'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^careers_units/$', views.careers_units, name='careers_units'),
    url(r'^careers_units/detail$', views.careers_units_detail, name='careers_detail'),
    url(r'^careers_cluster/$', views.careers_cluster, name='careers_cluster'),

    url(r'^special/sweetbox/$', views.sweetbox, name='special_sweetbox'),
    url(r'^special/4dx/$', views.show_4dx, name='special_4dx'),
    url(r'^special/dolby-atmos/$', views.dolby_atmos, name='special_dolby_atmos'),
    url(r'^special/imax/$', views.imax, name='special_imax'),
    url(r'^special/gold-class/$', views.gold_class, name='special_gold_class'),
    url(r'^special/lamour/$', views.lamour, name='special_lamour'),
    url(r'^special/starium/$', views.starium, name='special_starium'),
    url(r'^special/premium/$', views.premium, name='special_premium'),
    url(r'^special/screenx/$', views.screenx, name='special_screenx'),
    url(r'', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





