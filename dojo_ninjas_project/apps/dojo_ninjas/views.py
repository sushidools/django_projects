# views.py
from apps.dojo_ninjas.models import *
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        "dojos": Dojo.objects.all()
    }
    return render(request, 'dojo_ninjas/index.html', context)