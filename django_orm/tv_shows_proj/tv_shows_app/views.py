from django.shortcuts import render, HttpResponse
from .models import Movie

# Create your views here.

def shows(request):
    context = {
        'shows': 'shows' # needs to be the queryset of all shows
    }
    return render(request, 'shows.html', context)

def new_show(request):
    return render(request, 'add_show.html')

def show_details(request, show_id):
    context = {
        'show': Movie.objects.get(id=show_id)
    }
    return render(request, 'show_details.html', context)

def edit_show(request, show_id):
    context = {
        'show': Movie.objects.get(id=show_id)
    }
    return render(request, 'edit_show.html', context)