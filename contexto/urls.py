from contexto.views import ContextoOriginalViewSet, ContextoViewSet
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
contexto_original_list = ContextoOriginalViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = format_suffix_patterns([
    path('', contexto_list, name='contexto-list'),
    path('<int:pk>', contexto_detail, name='contexto-detail'),
    path('original',contexto_original_list, name='contexto-original-detail')
])