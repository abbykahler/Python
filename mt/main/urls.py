from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('snare', views.snare),

    
    
]