from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from api_app import views

router = DefaultRouter()
router.register(r'register', views.RegisterViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
