from django.shortcuts import render, HttpResponse,redirect

def index(request):
    return render(request, "index.html")

# Create your views here.
def processing_form_data(request):
    form_data = request.POST
    name = request.POST['name']
    dojolocation = request.POST['dojolocation']
    favoritelanguage = request.POST['favoritelanguage']
    comment = request.POST['comment']
    return redirect ('/success')

def success(request, name, dojolocation, favoritelanguage, comment):
    context = {
        'name':name,
        'dojolocation':dojolocation,
        'favoritelanguage': favoritelanguage,
        'comment': comment
        
    }
    return render(request, 'success.html',context)