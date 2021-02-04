from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request): 
    return HttpResponse("some string")

def blogs (request): 
    return HttpResponse("placeholder to later display a list of all blogs")

def blogs_new (request): 
    return HttpResponse("placeholder to display a new form to create a new blog")

def blogs_again (request): 
    return HttpResponse("routed")

def blogs_num (request, number): 
    return HttpResponse(f'placeholder to display blog number {number}')
    
def blogs_numb (request, number): 
    return HttpResponse(f'placeholder to edit blog number {number}')

def blogs_last (request, number): 
    return HttpResponse('display list of all blogs')

# def time(request):
#     context = {
#         "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
#     }
#     return render(request,'index.html', context)