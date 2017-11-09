from django.conf.urls import url, include
import views

urlpatterns = [

	url(r'^$', views.home, name='home'),
	url(r'^showing/$', views.showing, name='showing'),
	url(r'^comingsoon/$', views.coming_soon, name='comingsoon'),
	url(r'^film/detail/(?P<id>\d+)/$', views.film_detail, name='film_detail'),
	url(r'^news/$', views.news, name='news'),
    url(r'^new/detail/(?P<id>\d+)/$', views.new_detail, name='new_detail'),
    url(r'^cinema/technology/(?P<name>[-\w]+)/$', views.technology_detail, name='technology_detail'),
    url(r'^technology/$', views.get_technology, name='get_technology'),
    url(r'^posts/$', views.get_post, name='get_cms'),
    url(r'^contacts/$', views.contacts, name='contacts'),
]
