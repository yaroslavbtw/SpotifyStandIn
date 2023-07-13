# Generated by Django 4.2.3 on 2023-07-13 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0002_alter_artist_name_alter_genre_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='playlists',
        ),
        migrations.AddField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(related_name='playlist', through='Music.SongPlaylist', to='Music.song'),
        ),
    ]
