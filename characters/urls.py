from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from characters import views

urlpatterns = [
    path('characters/', views.CharacterList.as_view()),
    path('characters/<int:pk>', views.CharacterDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)