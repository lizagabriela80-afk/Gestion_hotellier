from django.shortcuts import render
from rooms.models import Room

def accueil(request):
    chambres_vedette = Room.objects.filter(disponibility=True)[:3]
    return render(request, 'coring/accueil.html', {'chambres_vedette': chambres_vedette})