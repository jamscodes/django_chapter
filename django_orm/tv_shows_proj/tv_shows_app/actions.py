from django.shortcuts import redirect
from django.db import models
from .models import Movie

def add_show(request):
    new_movie = Movie.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['rel_date'],
        desc = request.POST['desc']
    )
    return redirect(f'/shows/{new_movie.id}')

def edit_show(request):
    this_movie = Movie.objects.get(id=request.POST.get('show_id'))
    this_movie.title = request.POST['title']
    this_movie.network = request.POST['network']
    this_movie.release_date = request.POST.get('rel_date')
    this_movie.desc = request.POST['desc']
    this_movie.save()
    return redirect(f'/shows/{request.POST["show_id"]}/')

def delete_show(request, show_id):
    this_movie = Movie.objects.get(id=show_id)
    this_movie.delete()
    return redirect('/shows/')