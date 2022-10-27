from django.urls import include, path
from rest_framework import routers
from characters.views import CharacterViewSet
from contexto.views import ContextoViewSet

from auth_user.views import UserViewSet
from equipments.views import EquipmentViewSet
from professions.views import ProfessionsViewSet
from races.views import RacesViewSet
from statistics_user.views import StatisticsUserViewSet 


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'characters',CharacterViewSet)
router.register(r'professions',ProfessionsViewSet)
router.register(r'races',RacesViewSet)
router.register(r'equipments',EquipmentViewSet)
router.register(r'statistics',StatisticsUserViewSet)




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('contexto/', include('contexto.urls')),
]
