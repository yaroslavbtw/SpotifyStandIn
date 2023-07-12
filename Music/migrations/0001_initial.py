# Generated by Django 4.2.3 on 2023-07-12 00:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='data/albums_covers/')),
                ('release_date', models.DateField(auto_now_add=True)),
                ('album_type', models.CharField(choices=[('album', 'Album'), ('ep', 'EP'), ('single', 'Single')], default='album', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='data/artists_photo/')),
                ('verified', models.BooleanField(default=False)),
                ('followers', models.PositiveBigIntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='data/playlist_covers/')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('duration', models.DurationField()),
                ('audio_file', models.FileField(upload_to='data/audio_files/')),
                ('dt_create', models.DateField(auto_now_add=True)),
                ('listening', models.PositiveBigIntegerField(blank=True, default=0)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Music.album')),
                ('artists', models.ManyToManyField(related_name='songs', to='Music.artist')),
                ('genres', models.ManyToManyField(related_name='songs', to='Music.genre')),
            ],
        ),
        migrations.CreateModel(
            name='SongPlaylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateField(auto_now_add=True)),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Music.playlist')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Music.song')),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='playlists',
            field=models.ManyToManyField(related_name='songs', through='Music.SongPlaylist', to='Music.playlist'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Music.artist'),
        ),
    ]
