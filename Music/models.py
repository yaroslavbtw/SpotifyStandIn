from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    title = models.CharField(max_length=100, null=False)


class Album(models.Model):
    ALBUM_TYPE_CHOICES = (
        ('album', 'Album'),
        ('ep', 'EP'),
        ('single', 'Single'),
    )
    title = models.CharField(max_length=200, null=False)
    cover = models.ImageField(upload_to='data/albums_covers/', blank=True, null=True)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, null=False)
    release_date = models.DateField(auto_now_add=True)
    album_type = models.CharField(max_length=10, choices=ALBUM_TYPE_CHOICES, default='album')


class Artist(models.Model):
    name = models.CharField(max_length=100, null=False)
    photo = models.ImageField(upload_to='data/artists_photo/', blank=True, null=True)
    verified = models.BooleanField(default=False, null=False)
    followers = models.PositiveBigIntegerField(default=0, blank=True, null=False)


class Song(models.Model):
    title = models.CharField(max_length=100, null=False)
    artists = models.ManyToManyField('Artist', related_name='songs')
    album = models.ForeignKey('Album', on_delete=models.DO_NOTHING, null=True, blank=True)
    duration = models.DurationField(null=False)
    genres = models.ManyToManyField('Genre', related_name='songs')
    audio_file = models.FileField(upload_to='data/audio_files/', null=False)
    playlists = models.ManyToManyField('Playlist', related_name='songs', through='SongPlaylist',
                                       through_fields=('song', 'playlist', 'added_at'))
    dt_create = models.DateField(auto_now_add=True, editable=False)
    listening = models.PositiveBigIntegerField(default=0, null=False, blank=True)


class Playlist(models.Model):
    title = models.CharField(max_length=200, null=False)
    cover = models.ImageField(upload_to='data/playlist_covers/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length=255, null=True, blank=True)


class SongPlaylist(models.Model):
    song = models.ForeignKey('Song', on_delete=models.DO_NOTHING, null=False)
    playlist = models.ForeignKey('Playlist', on_delete=models.DO_NOTHING, null=False)
    added_at = models.DateField(auto_now_add=True)
