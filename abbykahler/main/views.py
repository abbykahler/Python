from django.shortcuts import render, redirect
import random
from datetime import datetime 


# from collection.forms import ContactForm



def index(request):
    return render(request,'index.html')

def ninjaman(request):
    return render(request, 'ninjaman.html')

def airplane(request):
    return render(request, 'airplane.html')

def work(request):
    return render(request, 'work.html')

def education(request):
    return render(request, 'education.html')

def contact(request):
    # form_class = ContactForm
    return render(request, 'index.html', {
        # 'form': form_class,
    })

