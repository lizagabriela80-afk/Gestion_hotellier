from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.mes_reservations, name='mes_reservations'),
]