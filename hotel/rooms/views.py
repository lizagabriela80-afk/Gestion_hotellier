from django.shortcuts import render, get_object_or_404
from .models import Room

def liste_chambres(request):
    chambres = Room.objects.filter(disponible=True)
    return render(request, 'rooms/liste_chambres.html', {'chambres': chambres})

def detail_chambre(request, chambre_id):
    chambre = get_object_or_404(Room, id=chambre_id)
    return render(request, 'rooms/detail_chambre.html', {'chambre': chambre})