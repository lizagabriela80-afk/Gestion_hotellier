from django.db import models
from django.contrib.auth.models import User
from rooms.models import Room

class Booking(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    chambre = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_arrivee = models.DateField()
    date_depart = models.DateField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.username} - {self.chambre.nom}"