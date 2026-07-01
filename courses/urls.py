from django.urls import path
from .views import kurslar , salomlash


urlpatterns = [
    path('', salomlash),
    path('kurslar', kurslar),
]