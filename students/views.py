from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ismi(request):
    return HttpResponse("Studentlar : Ali , Norbek , Guli ")

def yoshi(request):
    return HttpResponse("Studentlar : Ali - 19 , Norbek - 21 , Guli - 20")

def malumoti(request):
    return HttpResponse(""" Ali - o'rta ma'lumotli
                            Norbek - oliy ma'lumotli
                            Guli - oliy ma'lumotli 
    """)
