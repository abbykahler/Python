from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('success', views.success),
    path('failure', views.failure),
    path('logout', views.logout),
    path('login', views.login),
]