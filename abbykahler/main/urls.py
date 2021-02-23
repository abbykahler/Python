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


    # path('register', views.register),
    # path('success', views.success),
    # path('failure', views.failure),
    # path('logout', views.logout),
    # path('login', views.login),
    # path('dashboard', views.dashboard),
    # path('trips/new', views.add_trip),
    # path('trips/create', views.create),
    # path('trips/<int:trip_id>', views.view_trip),
    # path('trips/<int:trip_id>/edit', views.edit_trip),
    # path('trips/<int:trip_id>/save', views.save),
    # path('trips/<int:trip_id>/update', views.update_trip),
    # path('trips/<int:trip_id>/delete', views.delete_trip),
]