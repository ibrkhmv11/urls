from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def ustoz_ismi(request):
    return HttpResponse("Sharafov Shahriyor")

def yoshi(request):
    return HttpResponse("23")

def malunoti(request):
    return HttpResponse("oliy")

def city(request):
    return HttpResponse("Buxoro")