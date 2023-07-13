from django.urls import path, include
from rest_framework import routers

from .views import SongViewSet, GenreViewSet, ArtistViewSet, PlaylistViewSet

router = routers.DefaultRouter()
router.register(r'song', SongViewSet)
router.register(r'genre', GenreViewSet)
router.register(r'artist', ArtistViewSet)
router.register(r'playlist', PlaylistViewSet)

urlpatterns = [
    path('', include(router.urls))
]
