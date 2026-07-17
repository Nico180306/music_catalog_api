from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=150)
    nationality = models.CharField(max_length=100, blank=True)
    formed_date = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Album(models.Model):
    # Relación 1:N -> Un artista tiene muchos álbumes
    artist = models.ForeignKey(
        Artist, 
        on_delete=models.CASCADE, 
        related_name='albums', 
        verbose_name="Artista"
    )
    title = models.CharField(max_length=200, verbose_name="Título del Álbum")
    release_date = models.DateField(verbose_name="Fecha de Lanzamiento")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio ($)")
    cover_url = models.URLField(blank=True, verbose_name="URL de Portada")

    def __str__(self):
        return f"{self.title} - {self.artist.name}"