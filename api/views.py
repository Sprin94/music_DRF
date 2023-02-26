from rest_framework.viewsets import ModelViewSet

from .serializers import SongSerializer, AlbumSerializer, SingerSerializer
from .models import Singer, Album, Song


class SingerViewSet(ModelViewSet):
    serializer_class = SingerSerializer
    queryset = Singer.objects.all()


class AlbumViewSet(ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()


class SongViewSet(ModelViewSet):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
