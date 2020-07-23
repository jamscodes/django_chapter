from django.shortcuts import render, HttpResponse

# Create your views here.

def generate_rand_string(request):
    return HttpResponse('We\'re on the right page')