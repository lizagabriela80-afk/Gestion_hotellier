from django.shortcuts import render, get_object_or_404
from .models import Room
from rest_framework import viewsets
from .serializers import RoomSerializer


def liste_chambres(request):
    chambres = Room.objects.filter(disponibility=True).order_by('type_chambre', 'nom')

    q = request.GET.get('q')
    if q:
        chambres = chambres.filter(nom__icontains=q)

    type_chambre = request.GET.get('type_chambre')
    if type_chambre:
        chambres = chambres.filter(type_chambre=type_chambre)

    return render(request, 'rooms/liste_chambres.html', {'chambres': chambres})


def detail_chambre(request, chambre_id):
    chambre = get_object_or_404(Room, id=chambre_id)
    return render(request, 'rooms/detail_chambre.html', {'chambre': chambre})



class RoomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer