from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.

def index(request):
    context = {
        'dojos': Dojo.objects.all(),
    }
    return render(request, 'home.html', context)

def add_dojo(request):
    Dojo.objects.create(
        name=request.POST['d_name'],
        city=request.POST['d_city'],
        state=request.POST['d_state']
    )
    return redirect('/')

def add_ninja(request):
    Ninja.objects.create(
        dojo_id=Dojo.objects.get(id=request.POST.get('dojo', False)),
        first_name=request.POST['n_f_name'],
        last_name=request.POST['n_l_name']
    )
    return redirect('/')

def delete_dojo(request, id):
    del_dojo = Dojo.objects.get(id=id)
    del_dojo.delete()
    return redirect('/')
