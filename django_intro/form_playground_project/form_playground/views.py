from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def form_handler(request):
    context = {
        'field_1': request.POST['one'],
        'field_2': request.POST['two']
    }
    return render(request, 'form_submitted.html', context)