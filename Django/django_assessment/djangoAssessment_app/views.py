from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactForm

def greeting(request, firstname=None):
    return render(request, 'greeting.html', {'firstname': firstname})




def infoPage(request):
    return render(request, 'djangoInfo.html')



def index(request):
    return render(request, 'index.html')



def personalGreeting(request, name):
    return render(request, 'index.html', {'name': name})



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            phone = form.cleaned_data['phone']
            streetaddress = form.cleaned_data['streetaddress']
            state = form.cleaned_data['state']
            zip_code = form.cleaned_data['zip']

            return HttpResponseRedirect(reverse('confirmation') + f'?firstname={firstname}&lastname={lastname}&phone={phone}&streetaddress={streetaddress}&state={state}&zip={zip_code}')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})



        
def confirmation(request):
    firstname = request.GET.get('firstname')
    lastname = request.GET.get('lastname')
    phone = request.GET.get('phone')
    streetaddress = request.GET.get('streetaddress')
    state = request.GET.get('state')
    zip_code = request.GET.get('zip')

    return render(request, 'confirmation.html', {
        'firstname': firstname,
        'lastname': lastname,
        'phone': phone,
        'streetaddress': streetaddress,
        'state': state,
        'zip': zip_code,
    })

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        if username == 'admin' and password == 'password':
            request.session['logged_in'] = True
            return HttpResponseRedirect(reverse('admin'))
        else:
            error_message = "Access Denied: Please login to access the admin panel"
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html', {})
    

def admin(request):
    if request.session.get('logged_in'):
        return render(request, 'admin.html', {'is_logged_in': True})
    else:
        return redirect('/login')