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
    url(r'^grappelli', include('grappelli.urls')),
    url(r'^admin', admin.site.urls),
    url(r'^$', views.home),
    url(r'^comingsoon/$', views.comingsoon),
    url(r'^cinox/$', views.cinox),
    url(r'^gift_card/$', views.gift_card),
    url(r'^membership/$', views.membership),
    url(r'^movie_voucher/$', views.movie_voucher),
    url(r'^account_create/$', views.account_create),
    url(r'^account_login/$', views.account_login),
    url(r'^arthouse/$', views.arthouse),
    url(r'^showing/$', views.showing),
    url(r'^special/sweetbox/$', views.sweetbox),
    url(r'^special/4dx/$', views.show_4dx),
    url(r'^special/dolby-atmos/$', views.dolby_atmos),
]

if settings.DEBUG:
    urlpatterns += urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



