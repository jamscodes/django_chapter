from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def form_handler(request):
    context = {
        'name': request.POST['name'],
        'fav_rock': request.POST['fav_rock'],
        'mult_fav_rock': request.POST.get('mult_fav_rock', False),
        'past_pet_rock': request.POST.get('past_pet_rock', False),
        'cur_pet_rock': request.POST.get('cur_pet_rock', False),
        'message': request.POST['message']
    }
    return render(request, 'form_submitted.html', context)