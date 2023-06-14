from django.shortcuts import render

# Create your views here.

def dummy(request):
    return render(request,'dummy.html')

def home(request):
    return render(request,'home.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')