from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'info-index.html')

def infoIndex(request):
    info_data = {
        'first_name': 'Ebonee',
        'last_name': 'Singleteary',
        'favorite_food': 'Gumbo',
        'vacation_destination': 'New Orleans'
}
    return render(request, 'info-index.html', {'info_data': info_data})

def infoForm(request):
    return render(request, 'info-form.html')


def formData(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        favorite_food = request.POST.get('favoritefood')
        return render(request, 'form-data.html', {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'favorite_food': favorite_food
        })
   
    return redirect('index') 