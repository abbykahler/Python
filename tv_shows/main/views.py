from django.shortcuts import render, redirect, HttpResponse
from .models import Show, TvManager
from django.contrib import messages


def index(request):
    
    return redirect('/shows')

def AddNewShow(request):  
    context = {
        'shows' : Show.objects.all()
    }
    return render(request, 'addNewShow.html', context)

def CreateNewShow(request):
    errors = Show.objects.show_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/shows/new')
    else:
        Show.objects.create(
            title=request.POST['title'], 
            network=request.POST['network'], 
            release_date=request.POST['release_date'], 
            description=request.POST['description'])
    
    return redirect(f'/shows')


def AllShows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'allShows.html', context)


def TvShow(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'tvShow.html', context)


def EditShow(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'editShow.html', context)

def UpdateShow(request, id):
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect(f'/shows/{{ show.id }}/update')
    else:
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
    return redirect(f'/shows/{id}')


def DeleteShow(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')

