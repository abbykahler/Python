from django.urls import path
from.import views

urlpatterns = [
    path('', views.index),
    path('blogs', views.blogs),
    path('blogs/new', views.blogs_new),
    path('blogs/create', views.blogs_again),
    path('blogs/<number>', views.blogs_num),
    path('blogs/<number>/edit', views.blogs_numb),
    path('blogs/<number>/delete', views.blogs_last),
]

