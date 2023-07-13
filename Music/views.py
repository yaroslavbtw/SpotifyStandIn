from django.db import transaction
from django.shortcuts import render
from rest_framework import viewsets

from Music.models import Song, Artist, Genre, Playlist
from Music.serializers import SongSerializer, ArtistSerializer, GenreSerializer, PlaylistSerializer, \
    SongOutputSerializer, PlaylistOutputSerializer


# Create your views here.

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return SongOutputSerializer
        return SongSerializer

    def perform_destroy(self, instance):
        # with transaction.atomic():
        #     song = Song.objects.get(id='e8674d13-b5e5-4713-867f-40585c453fed')
        #     song_artists = SongArtists.objects.filter(song=song)
        #     song_artists.delete()
        #     song.delete()
        instance.delete()


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PlaylistOutputSerializer
        return PlaylistSerializer
