import base64
from django.core.files.base import ContentFile
from rest_framework import serializers
from .models import Artist, Album

class AlbumSerializer(serializers.ModelSerializer):
    artist_name = serializers.ReadOnlyField(source='artist.name')
    cover = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Album
        fields = ['id', 'artist', 'artist_name', 'title', 'release_date', 'cover']

    def validate_cover(self, value):
        if value and ';base64,' in value:
            try:
                format, imgstr = value.split(';base64,')
                ext = format.split('/')[-1]
                return ContentFile(
                    base64.b64decode(imgstr),
                    name=f'album_cover.{ext}'
                )
            except Exception:
                raise serializers.ValidationError("La imagen no se encuentra con base64 válida.")
        return value

class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)
    photo = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Artist
        fields = ['id', 'name', 'nationality', 'formed_date', 'bio', 'photo', 'albums']

    def validate_photo(self, value):
        if value and ';base64,' in value:
            try:
                format, imgstr = value.split(';base64,')
                ext = format.split('/')[-1]
                return ContentFile(
                    base64.b64decode(imgstr),
                    name=f'artist_photo.{ext}'
                )
            except Exception:
                raise serializers.ValidationError("La imagen no se encuentra con base64 válida.")
        return value