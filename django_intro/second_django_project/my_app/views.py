from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

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

def linked_page(request):
    return render(request, 'linked-page.html')

def display_values(request):
    context = {
        'first_name': 'Jonathan',
        'last_name': 'Moore',
        'email': 'jmoore.codes@gmail.com'
    }
    return render(request, 'display-values.html', context)