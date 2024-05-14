from django.shortcuts import render, redirect
from .models import Trip, CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView



def main_page(request):
    return render(request, 'main.html')

def destination_page(request):
    return render(request, 'destination.html')

@login_required
def travels_page(request):
    user = request.user
    user_trips = Trip.objects.filter(user=user)
    other_user_trips = Trip.objects.exclude(user=user)
    context = {
        'name': user.name,  
        'user_trips': user_trips,
        'other_user_trips': other_user_trips,
    }
    return render(request, 'travels.html', context)


def add_trip_page(request):
    return render(request, 'add.html')

def add_trip(request):
    if request.method == 'POST':
        destination = request.POST.get('destination')
        description = request.POST.get('description')
        from_datetime = request.POST.get('from_datetime')
        to_datetime = request.POST.get('to_datetime')
        
        Trip.objects.create(
            destination=destination,
            description=description,
            from_datetime=from_datetime,
            to_datetime=to_datetime
        )

        return redirect('travels_page')

    return render(request, 'add.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        pw_confirmation = request.POST.get('pw_confirmation')

        if password != pw_confirmation:
            pass

        if len(password) < 8:
            pass

        if CustomUser.objects.filter(username=username).exists():
            pass

        user = CustomUser.objects.create_user(username=username, password=password, name=name)
        return redirect('login')

    return render(request, 'main.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('travels_page')
    else:
        return LoginView.as_view()(request)