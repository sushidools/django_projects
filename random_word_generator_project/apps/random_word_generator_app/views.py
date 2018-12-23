from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string

def index(request):
    return redirect('/random_word')

def random_word(request):
    if not 'count' in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    
    request.session['random_string'] = get_random_string(length=14)


    return render(request,'random_word_generator_app/index.html', request.session)

def reset(request):
    del request.session['count']
    
    return redirect('/')