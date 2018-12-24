# views.py
from apps.users_login_app.models import *
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, 'users_login_app/all_users.html', context)

def new(request):
    return render(request, "users_login_app/create_user.html")

def create(request):
    if request.POST:
        if User.objects.valid_user(request=request):
            user = User(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], age=request.POST['age'])
            if user:
                user.save()
                url = "/users/" + str(User.objects.last().id)
            else:
                return redirect("/users")
        else:
            url = "/users"

        return redirect(url)
    else:
        return redirect("/users")   

def edit(request, id):
    context = {
        "user": User.objects.get(id=int(id))
    }
    return render(request, "users_login_app/edit_user.html", context)\

def destroy(request, id):
    b = User.objects.get(id=int(id))
    b.delete()
    return redirect("/users")

def update(request):
    if request.POST:
        user = User.objects.get(id=int(request.POST['id']))
        if user:
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            url="/users/" + request.POST['id']
        else:
            url = "/users"
        return redirect(url)
    else:
        return redirect("/users")

def show(request, id):
    context = {
        "user": User.objects.get(id=int(id))
    }
    return render(request, "users_login_app/user.html", context)