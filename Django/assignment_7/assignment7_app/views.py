from django.shortcuts import render, redirect, get_object_or_404
from .models import User

def submit_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        dietary_preference = request.POST.get('dietary_preference')
        User.objects.create(name=name, height=height, weight=weight, dietary_preference=dietary_preference)
        return redirect('homepage')
    return render(request, 'user_form.html')


def homepage(request):
    users = User.objects.all()  
    return render(request, 'homepage.html', {'users': users})

def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'user_detail.html', {'user': user})