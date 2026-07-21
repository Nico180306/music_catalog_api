import base64
import uuid
from django.core.files.base import ContentFile
from rest_framework import serializers
from .models import Artist, Album

class AlbumSerializer(serializers.ModelSerializer):
    artist_name = serializers.ReadOnlyField(source='artist.name')
    # Añadimos allow_null=True para que al editar sin tocar la imagen no falle por recibir null
    cover = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    class Meta:
        model = Album
        fields = ['id', 'artist', 'artist_name', 'title', 'release_date', 'cover']

    def validate_cover(self, value):
        if value and isinstance(value, str) and ';base64,' in value:
            try:
                format, imgstr = value.split(';base64,')
                ext = format.split('/')[-1]
                # Limpiamos la extensión por si viene con parámetros extra en el Base64
                ext = ext.split(';')[0]
                
                # Generamos un nombre único con UUID para evitar que el navegador cachee la foto vieja o colisionen archivos
                unique_filename = f'album_cover_{uuid.uuid4().hex[:8]}.{ext}'
                
                return ContentFile(
                    base64.b64decode(imgstr),
                    name=unique_filename
                )
            except Exception:
                raise serializers.ValidationError("La imagen no se encuentra con base64 válida.")
        return value

class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)
    photo = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    class Meta:
        model = Artist
        fields = ['id', 'name', 'nationality', 'formed_date', 'bio', 'photo', 'albums']

    def validate_photo(self, value):
        if value and isinstance(value, str) and ';base64,' in value:
            try:
                format, imgstr = value.split(';base64,')
                ext = format.split('/')[-1]
                ext = ext.split(';')[0]
                
                # Nombre único para cada foto de artista que se suba
                unique_filename = f'artist_photo_{uuid.uuid4().hex[:8]}.{ext}'
                
                return ContentFile(
                    base64.b64decode(imgstr),
                    name=unique_filename
                )
            except Exception:
                raise serializers.ValidationError("La imagen no se encuentra con base64 válida.")
        return value