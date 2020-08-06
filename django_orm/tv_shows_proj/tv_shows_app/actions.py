from django.shortcuts import redirect
from django.db import models
from .models import Movie

def add_show(request):
    Movie.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['rel_date'],
        desc = request.POST['desc']
    )
    # show_id = Movie.objects.get(id = new_movie.id)
    return redirect(f'/shows/')

def edit_show(request):
    this_movie = Movie.objects.get(id=request.POST.get('show_id'))
    this_movie.title = request.POST['title']
    this_movie.network = request.POST['network']
    this_movie.release_date = request.POST.get('release_date')
    this_movie.desc = request.POST['desc']
    this_movie.save()
    return redirect(f'/shows/{request.POST["show_id"]}')