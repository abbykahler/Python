from django.shortcuts import render ,redirect
from .models import User, Messages, Comment
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')

def login(request) :
    if request.POST['type']=="register" :
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items() :
                messages.error(request,value)
            return redirect('/')
        else :
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            User.objects.create(first_name=request.POST['first_name'],
                                last_name=request.POST['last_name'],
                                email=request.POST['email'],
                                password=pw_hash
            )
            user = User.objects.last()
            request.session['userid'] = user.id
            return redirect('/wall')
    elif request.POST['type']=="login" :
        user = User.objects.filter(email=request.POST['email'])
        if user :
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['userid'] = logged_user.id 
                return redirect('/wall')
            else :
                messages.error(request,"E-mail or Password is incorrect")
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

# def post(request):
#     Messages.objects.create(
#         message = request.POST['message'],
#         author = User.objects.get(id=request.session['user_id'])
#     )
#     return redirect('/dashboard')

def post(request, post_id):
    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'post' : Messages.objects.get(id=post_id),
        'comments' : Comment.objects.order_by('id')
    }
    return render(request,'index.html', context)



def comment(request) :
    user = User.objects.get(id=request.session['user_id'])
    post = Messages.objects.get(id=request.POST['message_id'])
    Comment.objects.create(
        comment= request.POST['comment'], 
        user_id= user, 
        message_id= messages)
    return redirect('/dashboard')


