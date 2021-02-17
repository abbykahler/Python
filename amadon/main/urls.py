from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('amadon', views.store),
    path('process', views.process),
    path('amadon/checkout', views.checkout),
]