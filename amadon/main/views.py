from django.shortcuts import redirect,render
from .models import Store

def index(request):
    return redirect('/amadon')

def store(request):
    
    if 'items' not in request.session:
        request.session['items'] = 0
            
    if 'price' not in request.session:
        request.session['price'] = 0
            
    if 'total' not in request.session:
        request.session['total'] = 0
    amadonstore ={
        'items' : Store.objects.all()
    }
    return render(request, 'store.html', amadonstore)



def process(request):
    amount = Store.objects.get(id=request.POST['id'])
    # request.session['item'] += int(request.POST['quantity'])
    request.session['price'] = float(request.POST['quantity']) * float(amount.price)
    request.session['total'] += request.session['price']
    return redirect('/amadon/checkout')


def checkout(request):
    context={
        'price':request.session['price'],
        'total':request.session['total'],
        'items':request.session['items']
    }
    return render(request, 'checkout.html', context)

