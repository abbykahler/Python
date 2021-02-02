from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
# import bcrypt

def index(request):
    print(User.objects.all())
    return render(request,'index.html')



def register(request):    
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for msg in errors.values(): 
            messages.error(request, msg)
            
        return redirect('/')
    
    new_user = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=request.POST['password'],
    )
    
    request.session['user_id'] = new_user.id
    return redirect('/success')



def success(request): 
    logged_in_user=User.objects.get(id=request.session['user_id'])
    context = {
        'logged_in_user' : logged_in_user
    }
    return render(request,'success.html',context)

def logout(request):
    request.session.flush()
    return redirect('/')