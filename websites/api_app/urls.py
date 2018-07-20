from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from api_app import views

router = DefaultRouter()
router.register(r'blogs', views.BlogViewSet)
router.register(r'faqs', views.FaqViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^transaction_history/$', views.TransactionHistoryList.as_view(), name="transaction-history-list"),
    url(r'^register/', views.register, name="register"),
    url(r'^profile/', views.ProfileDetail.as_view(), name="profile"),
    url(r'^movie/seats$', views.get_movie_seat, name="movie-seat"),
    url(r'^check/seats/$', views.check_movie_seat, name="check-seat"),
    url(r'^verify/card_member/$', views.verify_card_member, name="verify-card-member"),
    url(r'^get/card_member/$', views.get_card_member, name="get-card-member"),
    url(r'^movie/showing/$', views.ShowingList.as_view(), name="showing"),
    url(r'^movie/comming/$', views.CommingList.as_view(), name="comming"),
    url(r'^movie/(?P<pk>\d+)/$', views.DetailMovie.as_view(), name="detail-movie"),


]
