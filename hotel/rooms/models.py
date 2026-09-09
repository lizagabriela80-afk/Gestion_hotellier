from django.db import models

class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Simple'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    ]
    nom = models.CharField(max_length=100)
    type_chambre = models.CharField(max_length=20, choices=ROOM_TYPES)
    description = models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    capacity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='rooms/', blank=True, null=True)
    disponibility = models.BooleanField(default=True)

    def __str__(self):
        return self.nom