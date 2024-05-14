from django.shortcuts import render

from django.shortcuts import render, redirect
from django.utils import timezone
import datetime





def index(request):

    return render(request,'index.html')

def dateAndTime(request):
    current_datetime = timezone.now()
    current_datetime = datetime.datetime.now()
    return render(request,'DateandTime.html', {'current_datetime': current_datetime} )