from rest_framework.serializers import (
    ModelSerializer, PrimaryKeyRelatedField, StringRelatedField)

from .models import Singer, Album, Song


class SingerSerializer(ModelSerializer):
    class Meta:
        model = Singer
        fields = ('name',)


class AlbumSerializer(ModelSerializer):
    singer = StringRelatedField()

    class Meta:
        model = Album
        fields = ('singer', 'release_year')


class SongSerializer(ModelSerializer):
    albums = StringRelatedField(
        many=True,
    )

    class Meta:
        model = Song
        fields = ('name', 'albums')
