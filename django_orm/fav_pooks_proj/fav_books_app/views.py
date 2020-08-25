from django.shortcuts import render, redirect
from .models import Book
from login_app.models import User

# Create your views here.

def index(request):
    if 'logged_user_id' in request.session:
        context = {
            'logged_user': User.objects.get(id=request.session['logged_user_id']),
            'books': Book.objects.all()
        }
        return render(request, 'books.html', context)
    return redirect('/')

def book_details(request, book_id):
    if 'logged_user_id' in request.session:
        context = {
            'book': Book.objects.get(id=book_id)
        }
        return render(request, 'book_details.html', context)
    return redirect('/')

def edit_book(request, book_id):
    if 'logged_user_id' in request.session and request.session['logged_user_id'] == Book.objects.get(id=book_id).added_by.id:
        context = {
            'book': Book.objects.get(id=book_id)
        }
        return render(request, 'edit_book.html', context)
    return redirect('/books/')

def user_details(request):
    if 'logged_user_id' in request.session:
        context = {
            'user': User.objects.get(id=request.session['logged_user_id'])
        }
        return render(request, 'user_details.html', context)