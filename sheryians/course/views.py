from django.shortcuts import render
from .models import *

# Create your views here.


def get(re):
    data=Course.objects.all()
    return render(re,'home.html',{'data':data})

def courses(request):
    data=Course.objects.all()
    return render(request,'courses.html',{'data':data})

def sign(request):
    return render(request,'sign_in.html')

def home(request):
    return render(request,'home.html')

def course(request,id):
    data=Course.objects.get(id=id)
    return render(request,'course.html',{'data':data})