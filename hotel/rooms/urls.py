from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet

router = DefaultRouter()
router.register(r'api/chambres', RoomViewSet, basename='chambre-api')

app_name = 'rooms'

urlpatterns = [
    path('', views.liste_chambres, name='liste_chambres'),
    path('api/', include(router.urls)),
    path('<int:chambre_id>/', views.detail_chambre, name='detail_chambre'),
]

urlpatterns += router.urls