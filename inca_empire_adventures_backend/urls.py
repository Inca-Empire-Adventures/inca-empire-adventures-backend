from django.urls import include, path
from rest_framework import routers
from contexto.views import ContextoViewSet

from personaje.views import GroupViewSet, UserViewSet



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('contexto/', include('contexto.urls')),
    path('', include('races.urls')),
    path('', include('professions.urls')),
    path('', include('equipments.urls')),
    path('', include('characters.urls')),
]
