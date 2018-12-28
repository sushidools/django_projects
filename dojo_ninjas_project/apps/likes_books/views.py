# views.py
from apps.likes_books.models import *
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "Hello, this is your likes_books app!"
    return HttpResponse(response)