from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def kurslar(request):
    return HttpResponse("""
    Ona tili , Algebra , Ingliz tili , Rus tili
                          """)


def salomlash(request):
    return HttpResponse("""Assalomu alaykum , 
             Hush kelibsiz !!! 
             Kurslarimiz : 
             """)


