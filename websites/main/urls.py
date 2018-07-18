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
from django.contrib.admin.sites import AdminSite
from main import forms

# Register Admin Login Form (Custom)
AdminSite.login_form = forms.SecureAdminLoginForm


handler404 = 'main.views.custom_404'
handler500 = 'main.views.custom_500'

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'^api/', include('api_app.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^', include('registration.urls')),
    url(r'^', include('booking.urls')),
    url(r'^', include('vnpay_payment.urls')),
    url(r'', include('core.urls')),
    url(r'', include('internal_payment.urls')),
    url(r'404', views.custom_404, name="404"),
    url(r'500', views.custom_500, name="500"),
    
]

if settings.DEBUG:
    urlpatterns += urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





