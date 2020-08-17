from django.shortcuts import render, redirect
from .models import Message

# Create your views here.

def index(request):
    if 'logged_user_id' in request.session:
        context = {
            'messages': Message.objects.all()
        }
        return render(request, 'welcome.html', context)
    return redirect('/')