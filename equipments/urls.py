from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from equipments import views

urlpatterns = [
    path('equipments/', views.EquipmentList.as_view()),
    path('equipments/<int:pk>', views.EquipmentDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)