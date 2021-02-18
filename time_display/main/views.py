from django.shortcuts import render, HttpResponse
from time import gmtime, strftime


def time(request):
    context =  strftime("%Y-%m-%d %H:%M %p", gmtime())
    return HttpResponse ({context})


