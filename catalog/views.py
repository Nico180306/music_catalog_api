from rest_framework import viewsets
from .models import Album, Artist
from .serializers import ArtistSerializer, AlbumSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly  


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('name')
    serializer_class = ArtistSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('-release_date') 
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]