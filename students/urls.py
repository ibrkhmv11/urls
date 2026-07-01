from django.urls import path
from .views import ismi , yoshi , malumoti

urlpatterns = [
    path('ismlar', ismi),
    path('yoshi', yoshi),
    path('malumoti', malumoti),
]