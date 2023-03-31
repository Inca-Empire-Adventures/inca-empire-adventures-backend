from django.urls import include, path
from rest_framework import routers
from adventures.views import AdventureViewSet
from auth_user.views import RegisterUserView
from character_detail.views import CharacterDetailViewSet
from characters.views import CharacterViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from equipments.views import EquipmentViewSet
from item.views import ItemViewSet
from loop.views import LoopViewSet
from loop_detail.views import LoopDetailViewSet
from professions.views import ProfessionsViewSet
from ethnicity.views import EthnicityViewSet
from skills.views import SkillsViewSet
from statistics_user.views import StatisticsUserViewSet 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'characters', CharacterViewSet, basename='character')
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

    # URL para registrar nuevos usuarios
    path('api/register/', RegisterUserView.as_view(), name='register_user'),
    
    # URL para obtener el token JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # URL para refrescar el token JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
