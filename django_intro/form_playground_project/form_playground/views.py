from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def form_handler(request):
    request.session['name'], request.session['fav_rock'], request.session['mult_fav_rock'], request.session['past_pet_rock'], request.session['cur_pet_rock'], request.session['message'] = request.POST['name'], request.POST['fav_rock'], request.POST.get('mult_fav_rock', False), request.POST.get('past_pet_rock', False), request.POST.get('cur_pet_rock', False), request.POST['message']

    return redirect('/form_submitted/')

def form_submission(request):
    return render(request, 'form_submitted.html')