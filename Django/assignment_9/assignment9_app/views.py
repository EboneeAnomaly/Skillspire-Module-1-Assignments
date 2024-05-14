from django.shortcuts import render, redirect
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

def addUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')  
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

def createUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')  
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})


def userPage(request):
    return render (request, 'users.html') 
