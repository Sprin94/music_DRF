from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SongViewSet, AlbumViewSet, SingerViewSet

router = DefaultRouter()

router.register('songs', SongViewSet, basename='songs')
router.register('albums', AlbumViewSet, basename='albums')
router.register('singers', SingerViewSet, basename='singers')


urlpatterns = [
    path('v1/', include(router.urls))
]
