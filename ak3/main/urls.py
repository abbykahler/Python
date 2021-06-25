from django.urls import path
from . import views
# from collection import views


urlpatterns = [
    path('', views.index),
    path('ninjaman', views.ninjaman),
    path('airplane', views.airplane),
    path('trip', views.trip),

    
]
    
