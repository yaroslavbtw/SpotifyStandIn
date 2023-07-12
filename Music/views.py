from django.shortcuts import render
from rest_framework import viewsets

from Music.models import Song
from Music.serializers import SongSerializer


# Create your views here.


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

