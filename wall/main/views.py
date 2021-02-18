from django.shortcuts import render ,redirect
from .models import User, Messages, Comment
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.validations(request.POST)
    if errors:
        for field, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    User.objects.register(request.POST)
    new_user = User.objects.get(username=request.POST['username'])
    request.session['user_id'] = new_user.id
    return redirect('/dashboard')

def login(request):
    result = User.objects.authenticate(request.POST['username'], request.POST['password'])
    if result == False:
        messages.error(request,"Invalid Username/Password")
    else:
        user = User.objects.get(username = request.POST['username'])
        request.session['user_id'] = user.id
        return redirect('/dashboard')
    return redirect('/')

def dashboard(request):
    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'messages' : Messages.objects.order_by('-id')
    }
    return render(request, 'login.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def post(request):
    Messages.objects.create(
        message = request.POST['message'],
        author = User.objects.get(id=request.session['user_id'])
    )
    return redirect('/dashboard')

def post(request, post_id):
    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'post' : Messages.objects.get(id=post_id),
        'comments' : Comment.objects.order_by('id')
    }
    return render(request,'show.html', context)

def comment(request, post_id):
    user = User.objects.get(id=request.session['user_id'])
    post = Messages.objects.get(id=post_id)
    Comment.objects.create(
        comment = request.POST['comment'],
        author = user,
        message = post
    )
    return redirect('/dashboard')