from django.urls import path
from . import views
# from collection import views


urlpatterns = [
    path('', views.index),
    path('ninjaman', views.ninjaman),
    path('work', views.work),
    path('education', views.education),
    path('contact', views.contact),
    path('airplane', views.airplane),
    path('trip', views.trip),

    
]