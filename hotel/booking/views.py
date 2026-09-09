from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Booking

@login_required
def mes_reservations(request):
    reservations = Booking.objects.filter(client=request.user).order_by('-date_arrivee')
    return render(request, 'booking/mes_reservations.html', {'reservations': reservations})