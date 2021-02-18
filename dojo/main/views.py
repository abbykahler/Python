from django.shortcuts import render,redirect

def index(request):
    return render(request, "index.html")

def processing_form_data(request):
    form_data = request.POST
    name = request.POST['name']
    dojo_location = request.POST['dojolocation']
    favorite_language = request.POST['favoritelanguage']
    comment = request.POST['comment']
    return redirect ('/success')

def success(request, name, dojo_location, favorite_language, comment):
    context = {
        'name':name,
        'dojo_location':dojo_location,
        'favorite_language': favorite_language,
        'comment': comment
        
    }
    return render(request, 'success.html',context)