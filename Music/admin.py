from django.contrib import admin
from .models import Genre, Album, Artist, Song, Playlist, SongPlaylist

# Register your models here.
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(SongPlaylist)
