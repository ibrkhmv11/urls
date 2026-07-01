from django.urls import path
from .views import ustoz_ismi , yoshi , malunoti , city

urlpatterns = [
    path('yosh',yoshi),
    path('ism',ustoz_ismi),
    path('malumot',malunoti),
    path('tugilgan',city)
]