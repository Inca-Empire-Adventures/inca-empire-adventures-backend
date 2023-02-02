from django.urls import include, path
from rest_framework import routers
from adventures.views import AdventureViewSet
from character_detail.views import CharacterDetailViewSet
from characters.views import CharacterViewSet
from contexto.views import ContextoViewSet

from auth_user.views import UserViewSet
from equipments.views import EquipmentViewSet
from item.views import ItemViewSet
from loop.views import LoopViewSet
from loop_detail.views import LoopDetailViewSet
from professions.views import ProfessionsViewSet
from ethnicity.views import EthnicityViewSet
from skills.views import SkillsViewSet
from statistics_user.views import StatisticsUserViewSet 


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'characters', CharacterViewSet)
router.register(r'professions', ProfessionsViewSet)
router.register(r'ethnicity', EthnicityViewSet)
router.register(r'equipments', EquipmentViewSet)
router.register(r'statistics', StatisticsUserViewSet)
router.register(r'item', ItemViewSet)
router.register(r'character_detail', CharacterDetailViewSet)
router.register(r'skills', SkillsViewSet)
router.register(r'adventure', AdventureViewSet)
router.register(r'loop', LoopViewSet)
router.register(r'loop_detail', LoopDetailViewSet)




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('contexto/', include('contexto.urls')),
]
