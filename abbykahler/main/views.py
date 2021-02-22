from django.shortcuts import render, redirect
import random
from datetime import datetime 


def index(request):
    return render(request,'index.html')

def ninjaman(request):
    return render(request, 'ninjaman.html')

def work(request):
    return render(request, 'work.html')

def education(request):
    return render(request, 'education.html')

def contact(request):
    return render(request, 'contact.html')


# def register(request):    
#     errs = User.objects.register_validator(request.POST)
#     if len(errs) > 0:
#         for msg in errs.values(): 
#             messages.error(request, msg)
            
#         return redirect('/')
    
#     new_user = User.objects.create(
#         first_name=request.POST['first_name'],
#         last_name=request.POST['last_name'],
#         email=request.POST['email'],
#         password=request.POST['password'],
#     )
    
#     request.session['user_id'] = new_user.id
#     return redirect('/success')


# def success(request): 
#     logged_in_user = User.objects.get(id=request.session['user_id'])
#     context = {
#         'logged_in_user': logged_in_user
#     }
#     return render(request, 'dashboard.html', context)


# def failure(request):
#     logged_in_user = User.objects.get(id=request.session['user_id'])
#     context = {
#         'logged_in_user': logged_in_user
#     }
#     return render(request, '/', context)


# def logout(request):
#     request.session.flush()
#     return redirect('/')


# def login(request):  
#     errs = User.objects.login_validator(request.POST)
#     if errs:
#         for msg in errs.values(): 
#             messages.error(request, msg)
#         return redirect('/')
#     user_list = User.objects.filter(email=request.POST['email'])
#     if user_list:
#         our_user = user_list[0]
#         user_password = user_list[0].password
#         request.session['user_id'] = our_user.id
#         if user_password == request.POST['password']:
#             return redirect('/dashboard')
#         else:
#             messages.error(request, "Password incorrect!")
#             return redirect('/')
#     else:   
#         print('no user found')
#         messages.error(request, "User not found!")
#         return redirect('/dashboard')


# def dashboard(request):
#     current_user = User.objects.get(id=request.session['user_id'])
#     current_user_added_trips = current_user.added_trips.all()
#     current_user_created_trips = current_user.created_trips.all()
    
#     context = {
#         'current_user': current_user,
#         'current_user_added_trips': current_user_added_trips,
#         'current_user_created_trips': current_user_created_trips,
#     }

#     return render(request, 'dashboard.html', context)


# def create(request):

#     current_user = User.objects.get(id=request.session['user_id'])
#     trip_errors = Trip.objects.trip_validator(request.POST) 
    
#     if len(trip_errors) > 0:
#         for key, val in trip_errors.items():
#             messages.error(request, val)
#         return redirect('/trips/new')

#     new_trip = Trip.objects.create(
#         destination=request.POST['destination'],
#         start_date=request.POST['start_date'],
#         end_date=request.POST['end_date'],
#         plan=request.POST['plan'],
#         user_trip=current_user,
#     )

#     request.session['trip_id'] = new_trip.id
#     return redirect('/dashboard')

# def add_trip(request):   
#     current_user = User.objects.get(id=request.session['user_id'])
    
#     context = {
#         'current_user': current_user,
#     }
#     return render(request, 'create.html', context)


# def delete_trip(request, trip_id):

#     current_user = User.objects.get(id=request.session['user_id'])
#     current_trip = Trip.objects.get(id = trip_id)

#     if current_trip.user_trip != current_user:
#         messages.error(request, "You have not created this trip. You cannot remove it!")
#         return redirect('/dashboard')

#     current_trip.delete()

#     return redirect('/dashboard')


# def view_trip(request, trip_id):  
#     current_user = User.objects.get(id=request.session['user_id'])
#     current_trip = Trip.objects.get(id = trip_id)
    
#     current_trip_added_users = current_trip.other_users.all()
#     added_empty = True
#     if len(current_trip_added_users) > 0:
#         added_empty = False
#     context = {
#         'current_user': current_user,
#         'current_trip': current_trip,
#         'current_trip_added_users': current_trip_added_users,
#         'added_empty': added_empty
#     }

#     return render(request, 'view.html', context)


# def edit_trip(request, trip_id):
#     if 'user_id' not in request.session:
#         messages.error(request, "User must be logged in!")
#         return redirect('/')

#     current_user = User.objects.get(id = request.session['user_id'])
#     current_trip = Trip.objects.get(id = trip_id)
#     current_trip.start_date = current_trip.start_date.strftime('%Y-%m-%d')
#     current_trip.end_date = current_trip.end_date.strftime('%Y-%m-%d')

#     if current_trip.user_trip != current_user:
#         messages.error(request, "Trip must be created")
#         return redirect('/dashboard')

#     context = {
#         "current_user": current_user,
#         "current_trip": current_trip,
#         "trip_id": trip_id
#     }

#     return render(request, 'edit.html', context)


# def save(request, trip_id):
    
#     if not request.POST['destination'] or not request.POST['start_date'] or \
#             not request.POST['end_date'] or not request.POST['plan']:
#         messages.error(request, "Must update all fields!")
#         return redirect(f'/trips/{trip_id}/edit')
#     current_trip = Trip.objects.get(id=trip_id)
#     if request.POST['destination']:
#         current_trip.destination = request.POST['destination']
#     if request.POST['start_date']:
#         current_trip.start_date = request.POST['start_date']
#     if request.POST['end_date']:
#         current_trip.end_date = request.POST['end_date']
#     if request.POST['plan']:
#         current_trip.plan = request.POST['plan']
#     current_trip.save()
#     return redirect('/dashboard')
    
    
#     return redirect('/dashboard')


# def update_trip(request, trip_id):
#     if 'user_id' not in request.session:
#         messages.error(request, "Must be logged in!")
#         return redirect('/')

#     current_user = User.objects.get(id=request.session['user_id'])
#     current_trip = Trip.objects.get(id = trip_id)

#     if current_trip.created_by_user != current_user:
#         messages.error(request, "You have not created this trip. You cannot edit it!")
#         return redirect('/dashboard')

#     trip_errors = Trip.objects.basic_validator(request.POST)

#     if len(trip_errors) > 0:
#         for key, val in trip_errors.items():
#             messages.error(request, val)
#         return redirect(f'/trips/{trip_id}/edit')

#     current_trip.destination = request.POST['destination']
#     current_trip.start_date = request.POST['start_date']
#     current_trip.end_date = request.POST['end_date']
#     current_trip.plan = request.POST['plan']
#     current_trip.save()

#     return redirect('/dashboard')