from django.urls import path
from . import views

app_name = 'rooms'

urlpatterns = [
    path('', views.liste_chambres, name='liste_chambres'),
    path('<int:chambre_id>/', views.detail_chambre, name='detail_chambre'),
]