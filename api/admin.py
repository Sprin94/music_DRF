from django.contrib import admin

from .models import Album, Song, Singer


admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Singer)
