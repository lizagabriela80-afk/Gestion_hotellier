from django.shortcuts import render, get_object_or_404
from .models import Room

def liste_chambres(request):
    chambres_par_categorie = []

    for code, label in Room.ROOM_TYPES:
        chambres = Room.objects.filter(type_chambre=code)
        if chambres.exists():
            chambres_par_categorie.append({
                'label': label,
                'chambres': chambres,
            })

    return render(request, 'rooms/liste_chambres.html', {'chambres_par_categorie': chambres_par_categorie})

def detail_chambre(request, chambre_id):
    chambre = get_object_or_404(Room, id=chambre_id)
    return render(request, 'rooms/detail_chambre.html', {'chambre': chambre})