from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularSwaggerView, SpectacularRedocView, SpectacularAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'doc/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
    path(
        'redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
]
