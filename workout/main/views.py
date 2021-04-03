from django.shortcuts import render, redirect
import random
from datetime import datetime 


# from collection.forms import ContactForm

def index(request):
    return render(request,'index.html')

def abs(request):
    return render(request, 'abs.html')

def back(request):
    return render(request, 'back.html')

def bi(request):
    return render(request, 'bi.html')

def chest(request):
    return render(request, 'chest.html')

def legs(request):
    return render(request, 'legs.html', {
    })

def tri(request):
    return render(request, 'tri.html')

def shoulder(request):
    return render(request, 'shoulders.html')

