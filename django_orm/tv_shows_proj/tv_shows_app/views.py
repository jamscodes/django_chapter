from django.shortcuts import render, HttpResponse

# Create your views here.

def new_show(request):
    return render(request, 'add_show.html')

def show_details(request, show_id):
    context = {
        'show_id': show_id
    }
    return render(request, 'show_details.html', context)