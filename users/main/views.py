from django.shortcuts import render, redirect
from .models import User


def index(request):
    context = {
        'all_users': User.objects.all()
    }
    return render(request, "index.html", context)


def process(request):
    name = request.POST['name']
    email = request.POST['email']
    age = request.POST['age']
    User.objects.create(name = name, email= email, age= age)
    return redirect ('/')

