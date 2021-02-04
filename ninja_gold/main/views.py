from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 2
    return render(request, 'index.html')

def process(request, gold):
    if request.method == "POST":
        if request.POST['building'] == 'farm':
            gold = random.randint(10, 21)
            
        elif request.POST['building'] == 'cave':
            gold = random.randint(5, 11)
            
        elif request.POST['building'] == 'house':
            gold = random.randint(2,6)
            
        elif request.POST['building'] == 'casino':
            gold = random.randint(-50, 51)

    request.session['total_gold'] += gold
    return redirect('/')

def reset(request):
    if request.method == "POST":
        request.session['total_gold'] = 0
    return redirect('/')
