from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request, id):
    if id < 5:
        return HttpResponse(f"{id} is lesser than 5!")
    elif id > 5:
        return HttpResponse(f"{id} is greater than 5!")
    else:
        return HttpResponse(f"{id} is equal to 5!")

def other_index(request):
    return HttpResponse("This is another hello!")

def a_third(request):
    return HttpResponse("All the URL strings!")