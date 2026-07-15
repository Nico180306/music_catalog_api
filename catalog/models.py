from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=150)
    nationality = models.CharField(max_length=100, blank=True)
    formed_date = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name