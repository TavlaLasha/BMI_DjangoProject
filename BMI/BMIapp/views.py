from django.shortcuts import render

def index(request):
    return render(request, 'BMIapp/index.html')

def login(request):
    return render(request, 'BMIapp/login.html')

def register(request):
    return render(request, 'BMIapp/register.html')

def base(request):
    return render(request, 'BMIapp/base.html')

def statistics(request):
    return render(request, 'BMIapp/statistics.html')
