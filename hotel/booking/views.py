from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from rooms.models import Room

@login_required
def mes_reservations(request):
    reservations = Booking.objects.filter(client=request.user).order_by('-date_arrivee')
    return render(request, 'booking/mes_reservations.html', {'reservations': reservations})

@login_required
def reserver_chambre(request, chambre_id):
    chambre = get_object_or_404(Room, id=chambre_id)

    if not chambre.disponibility:
        messages.error(request, "Cette chambre n'est plus disponible.")
        return redirect('rooms:detail_chambre', chambre_id=chambre.id)

    if request.method == 'POST':
        date_arrivee = request.POST.get('date_arrivee')
        date_depart = request.POST.get('date_depart')

        if date_depart <= date_arrivee:
            messages.error(request, "La date de départ doit être après la date d'arrivée.")
            return redirect('rooms:detail_chambre', chambre_id=chambre.id)

        Booking.objects.create(
            client=request.user,
            chambre=chambre,
            date_arrivee=date_arrivee,
            date_depart=date_depart
        )

        chambre.disponibility = False
        chambre.save()

        messages.success(request, "Réservation confirmée !")
        return redirect('booking:mes_reservations')

    return redirect('rooms:detail_chambre', chambre_id=chambre.id)