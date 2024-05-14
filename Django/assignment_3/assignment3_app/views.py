from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def displayName(request):
    return render(request, 'display-name.html')


def favoriteFood(request):
    return render(request, 'favorite-food.html')

def favoriteVacation(request):
    return render(request, 'favorite-vacation.html')


