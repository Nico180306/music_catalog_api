# catalog/admin.py
from django.contrib import admin
from .models import Artist, Album

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'genre')
    search_fields = ('name', 'genre', 'bio')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', 'release_date')
    list_filter = ('artist', 'release_date')
    search_fields = ('title', 'artist__name')