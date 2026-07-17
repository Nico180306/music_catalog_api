"""
URL configuration for music_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catalog.views import ArtistViewSet, AlbumViewSet
from django.conf import settings
from django.conf.urls.static import static

# 1. Instanciamos el enrutador de Django REST Framework 
router = DefaultRouter()

# 2. Registramos ambas entidades en el router (generará el CRUD automático para las dos)
router.register(r'artists', ArtistViewSet, basename='artist')
router.register(r'albums', AlbumViewSet, basename='album')

# 3. Definimos las rutas del proyecto insertando el paquete de URLs del router
urlpatterns = [
    path('admin/', admin.site.urls),
    # Ruta nativa para emitir y validar tokens OAuth 2.0 (/o/token/)
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # Exponemos todo nuestro CRUD (tanto artistas como álbumes) bajo el prefijo /api/
    path('api/', include(router.urls)),
]

# Permite que Django sirva las imágenes físicas durante el desarrollo local
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)