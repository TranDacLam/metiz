from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
import forms as metiz_forms
import views


urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register_user, name='register'),
    url(r'^activate/(?P<activation_key>\w+)/$', views.confirm_activation, name='confirm-activation'),
    url(r'^password_reset/$', auth_views.password_reset, {"html_email_template_name":"registration/password_reset_email.html"}, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/update/$', views.update_profile, name='update_profile'),
    # url(r'^password_change/$', password_change,
    #     kwargs={'template_name': 'registration/password_change_form.html',
    #             'password_change_form': DHPasswordChangeForm}, name="password_change"),
    # url(r'^password_change/done$', password_change_done,
    #     kwargs={'template_name': 'registration/password_change_done.html'}, name="password_change_done"),
]