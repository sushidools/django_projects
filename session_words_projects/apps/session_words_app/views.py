from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.contrib import messages
def index(request):

    return render(request,'session_words_app/index.html')

def add(request):
    font = '30' if 'big_font' in request.POST else '20'
    if not 'data' in request.session:
        request.session['data'] = []
    temp_list = request.session['data']
    temp_list.append({
        "word": request.POST['word'],
        "color": request.POST['color'],
        "font": font,
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    })
    request.session['data'] = temp_list
    return redirect("/")
    
def clear(request):
    del request.session['data']
    return redirect("/")