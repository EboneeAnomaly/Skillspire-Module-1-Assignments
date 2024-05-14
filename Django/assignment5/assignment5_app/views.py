from django.shortcuts import render
from django.http import HttpResponse

def counter(request):
    return HttpResponse("Counter View")

def index(request):
    counter = request.session.get('counter', 0)
    counter += 1
    request.session['counter'] = counter

    return render(request, 'counter.html', {'counter': counter})

def numDisplay(request):
    counter = request.session.get('counter', 0)
    counter += 1
    request.session['counter'] = counter

    return render(request, 'counter.html', {'counter': counter})

def counterDouble(request):
    counter = request.session.get('counter', 0)
    counter *= 2
    request.session['counter'] = counter

    return render(request, 'counter_x2.html', {'counter': counter})


def counterReset(request):
    request.session['counter'] = 0
    return render(request, 'counter_x2.html', {'counter': 0})

