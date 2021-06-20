from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('snare', views.snare),
    path('press', views.press),
    path('tour', views.tour),
    path('contact', views.contact),

    
    
]