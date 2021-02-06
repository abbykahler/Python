from django.shortcuts import render,redirect, HttpResponse
from .models import Dojo, Ninja

def index(request):
    context = {
        'dojos' : Dojo.objects.all(),
        'ninjas' : Ninja.objects.all(),
    }
    return render(request, 'index.html', context)

def createDojo(request):
    Dojo.objects.create(
        name = request.POST['newDojo'],
        city = request.POST['city'],
        state =request.POST['state'],
    )
    return redirect('/')

def createNinja(request):
    Ninja.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        dojo = request.POST['dojo.name']
    )
    return HttpResponse('ok')