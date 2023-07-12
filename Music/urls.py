from django.urls import path, include
from rest_framework import routers

from .views import SongViewSet

router = routers.DefaultRouter()
router.register(r'song', SongViewSet)

urlpatterns = [
    path('', include(router.urls))
]
