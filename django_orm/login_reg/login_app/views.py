from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.

def index(request):
    return render(request, 'login.html')

def success(request):
    if 'logged_user' in request.session:
        return render(request, 'welcome.html')
    return redirect('/')

def register(request):
    errors = User.objects.reg_validation(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    password = request.POST['pw']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    User.objects.create(
        f_name = request.POST['f_name'],
        l_name = request.POST['l_name'],
        email = request.POST['email'],
        password = pw_hash
    )

    request.session['logged_user'] = User.objects.get(email = request.POST['email'])

    return redirect('/success/')

def login(request):
    pw = request.POST['pw']
    user = User.objects.filter(email = request.POST['email'])

    if len(user) > 0 and bcrypt.checkpw(pw.encode(), user[0].password.encode()):
        request.session['logged_user'] = user[0].f_name
        return redirect('/success/')
    else:
        messages.error(request, 'Email or password is incorrect')
        return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

