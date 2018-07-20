from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from api_app import views

router = DefaultRouter()
router.register(r'blogs', views.BlogViewSet)
router.register(r'faqs', views.FaqViewSet)
router.register(r'news', views.NewViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^transaction_history/$', views.TransactionHistoryList.as_view(), name="transaction-history-list"),
    url(r'^register/', views.register, name="register"),
    url(r'^profile/', views.ProfileDetail.as_view(), name="profile"),
    url(r'^movie/seats$', views.get_movie_seat, name="movie-seat"),
    url(r'^check/seats/$', views.check_movie_seat, name="check-seat"),
]
