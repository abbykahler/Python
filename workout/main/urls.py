from django.urls import path
from . import views
# from collection import views


urlpatterns = [
    path('', views.index),
    path('abs', views.abs),
    path('back', views.back),
    path('bi', views.bi),
    path('chest', views.chest),
    path('legs', views.legs),
    path('tri', views.tri),
    path('shoulder', views.shoulder),
    

]