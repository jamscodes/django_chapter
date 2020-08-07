from django.shortcuts import redirect
from django.db import models
from .models import Movie
from django.contrib import messages

def add_show(request):
    errors = Movie.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new/')

    new_movie = Movie.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['rel_date'],
        desc = request.POST['desc']
    )
    return redirect(f'/shows/{new_movie.id}')

def edit_show(request):
    errors = Movie.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{request.POST.get("show_id")}/edit/')

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