from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from professions import views

urlpatterns = [
    path('professions/', views.ProfessionList.as_view()),
    path('professions/<int:pk>', views.ProfessionDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)