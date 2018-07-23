from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from api_app import views

router = DefaultRouter()
router.register(r'blogs', views.BlogViewSet)
router.register(r'faqs', views.FaqViewSet)
router.register(r'news', views.NewViewSet)
router.register(r'favourite/news', views.FavouriteNewOfferViewSet, base_name='favourite_new')
router.register(r'favourite/movies', views.FavouriteMovieViewSet, base_name='favourite_movie')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^transaction_history/$', views.TransactionHistoryList.as_view(), name="transaction-history-list"),
    url(r'^register/', views.register, name="register"),
    url(r'^profile/', views.ProfileDetail.as_view(), name="profile"),
    url(r'^movie/seats$', views.get_movie_seat, name="movie-seat"),
    url(r'^check/seats/$', views.check_movie_seat, name="check-seat"),
    url(r'^payment/booking/$', views.payment_booking, name="app-payment-booking"),
    url(r'^payment/methods/$', views.payment_method, name="app-payment-method"),
    url(r'^verify/card/payment/$', views.verify_payment_card, name="app-verify-payment-card"),
    url(r'^forgot/password/$', views.forgot_password, name="app-forgot-password"),
    url(r'^verify/otp/$', views.verify_otp, name="app-verify-otp"),
    url(r'^resend/otp/$', views.resend_otp, name="app-resend-otp"),
]
