from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'login.html')

def success(request):
    return render(request, 'welcome.html')

def register(request):
    errors = User.objects.reg_validation(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    User.objects.create(
        f_name = request.POST['f_name'],
        l_name = request.POST['l_name'],
        email = request.POST['email'],
        password = request.POST.get('pw')
    )
    return redirect('/success/')