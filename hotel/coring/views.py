from django.shortcuts import render
from rooms.models import Room

def accueil(request):
    chambres_vedette = Room.objects.filter(disponible=True)[:3]
    return render(request, 'core/accueil.html', {'chambres_vedette': chambres_vedette})