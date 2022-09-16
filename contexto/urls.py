from contexto.views import ContextoViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

contexto_list = ContextoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
contexto_detail = ContextoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = format_suffix_patterns([
    path('', contexto_list, name='contexto-list'),
    path('<int:pk>', contexto_detail, name='contexto-detail'),
])