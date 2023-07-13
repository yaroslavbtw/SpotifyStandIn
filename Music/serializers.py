from rest_framework import serializers
from Users.serializers import UserSerializer
from Music.models import Song, Genre, Artist, Playlist


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    # genres = GenreSerializer(many=True)
    # artists = ArtistSerializer(many=True)

    class Meta:
        model = Song
        fields = '__all__'

    # def create(self, validated_data):
    #     genres_data = validated_data.pop('genres')
    #     artists_data = validated_data.pop('artists')
    #     song = Song.objects.create(**validated_data)
    #     print(genres_data, artists_data)
    #     for genre_data in genres_data:
    #         genre, _ = Genre.objects.get_or_create(name=genre_data['title'])
    #         song.genres.add(genre)
    #     for artist_data in artists_data:
    #         artist, _ = Artist.objects.get_or_create(name=artist_data['name'])
    #         song.artists.add(artist)
    #     return song


class SongOutputSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    artists = ArtistSerializer(many=True)

    class Meta:
        model = Song
        fields = '__all__'


class PlaylistOutputSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    songs = SongOutputSerializer(many=True)

    class Meta:
        model = Playlist
        fields = '__all__'
