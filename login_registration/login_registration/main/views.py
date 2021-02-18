from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
# import bcrypt


def index(request):
    return render(request,'index.html')


def register(request):    
    errs = User.objects.register_validator(request.POST)
    if len(errs) > 0:
        for msg in errs.values(): 
            messages.error(request, msg)
            
        return redirect('/')

    
    # password = request.POST('password')
    # hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
    # print(password)
    # print(hashed)
    
    new_user = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=request.POST['password'],
    )
    
    request.session['user_id'] = new_user.id
    return redirect('/success')


def success(request): 
    logged_in_user = User.objects.get(id=request.session['user_id'])
    context = {
        'logged_in_user': logged_in_user
    }
    return render(request, 'success.html', context)


def failure(request):
    logged_in_user = User.objects.get(id=request.session['user_id'])
    context = {
        'logged_in_user': logged_in_user
    }
    return render(request, context)


def logout(request):
    request.session.flush()
    return redirect('/')


def login(request):  
    errs = User.objects.login_validator(request.POST)
    if errs:
        for msg in errs.values(): 
            messages.error(request, msg)
        return redirect('/')
    user_list = User.objects.filter(email=request.POST['email'])
    if user_list:
        our_user = user_list[0]
        user_password = user_list[0].password
        request.session['user_id'] = our_user.id
        if user_password == request.POST['password']:
            return redirect('/success')
        else:
            messages.error(request, "Password incorrect!")
            return redirect('/')
    else:   
        print('no user found')
        messages.error(request, "User not found!")
        return redirect('/')
