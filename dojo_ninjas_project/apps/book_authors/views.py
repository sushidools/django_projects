# views.py
from apps.book_authors.models import *
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        "authors": Author.objects.all(),
        "books": Book.objects.all(),
    }
    return render(request, 'book_authors/book_index.html', context)