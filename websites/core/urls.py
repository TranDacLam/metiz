from django.conf.urls import url, include
import views


handler404 = 'core.views.custom_404'
handler500 = 'core.views.custom_500'

urlpatterns = [

	url(r'^showing/$', views.showing, name='showing'),
	url(r'^comingsoon/$', views.comingsoon, name='comingsoon'),
	url(r'^film/detail/(?P<id>\d+)/$', views.film_detail, name='film_detail'),
]
