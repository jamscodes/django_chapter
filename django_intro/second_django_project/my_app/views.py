from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return HttpResponse('Placeholder to later display a list of all blogs')

def new(request):
    return HttpResponse('Placeholder to display a new form to create a new blog')

def create(request):
    return redirect('/')

def show(request, blog_id):
    return HttpResponse(f"Placeholder to display blog number: {blog_id}")

def edit(request, blog_id):
    return HttpResponse(f"Placeholder to edit blog {blog_id}")

def delete(request, blog_id):
    return redirect('/')