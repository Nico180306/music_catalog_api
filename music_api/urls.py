"""
URL configuration for music_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Ruta nativa para emitir y validar tokens OAuth 2.0
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/', include('catalog.urls')),
]