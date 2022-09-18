from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from races import views

urlpatterns = [
    path('races/', views.RaceList.as_view()),
    path('races/<int:pk>', views.RaceDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)