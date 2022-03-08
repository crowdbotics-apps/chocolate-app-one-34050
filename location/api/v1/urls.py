from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CityViewSet

router = DefaultRouter()
router.register("city", CityViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
