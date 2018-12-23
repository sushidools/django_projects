from django.shortcuts import render, HttpResponse, redirect
def index(request):

    return render(request,'survey_form_app/index.html')

def process(request):

    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect("/result")
    else:
        return redirect("/")

def result(request):
    return render(request,'survey_form_app/index1.html', request.session)