from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def generate_rand_string(request):
    if 'a_count' in request.session:
        request.session['a_count'] += 1
    else:
        request.session['a_count'] = 1

    request.session['rand_string'] = get_random_string(length=14)
    
    return render(request, 'random_word.html')

def reset(request):
    request.session.flush()
    return redirect('/random_word/')