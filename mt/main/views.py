from django.shortcuts import render, redirect

def index(request):
    return redirect('/')

def home(request):  
    return render(request, 'home.html')

def snare(request):  
    return render(request, 'snare.html')

def press(request):  
    return render(request, 'press.html')

def tour(request):  
    return render(request, 'tour.html')

def contact(request):  
    return render(request, 'contact.html')

def about(request):  
    return render(request, 'about.html')


