from rest_framework import serializers
from .models import Artist, Album

# 1. PRIMERO definimos el álbum 
class AlbumSerializer(serializers.ModelSerializer):
    # Inyectamos el nombre del artista en el JSON para facilitarle la vida a React
    artist_name = serializers.ReadOnlyField(source='artist.name')

    class Meta:
        model = Album
        fields = ['id', 'artist', 'artist_name', 'title', 'release_date', 'price', 'cover_url']

# 2. DESPUÉS definimos el artista, anidando el AlbumSerializer
class ArtistSerializer(serializers.ModelSerializer):
    # Relación inversa: Trae el catálogo del artista en una sola llamada REST
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        # Campos exactos de models.py + la relación 'albums'
        fields = ['id', 'name', 'nationality', 'formed_date', 'bio', 'albums']