from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

# Create your views here.

def index(request):
    return HttpResponse("Go to /books or /authors")

def books(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'add_books.html', context)

def authors(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'add_authors.html', context)

def add_book(request):
    Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc']
    )
    return redirect('/books/')

def book_data(request, book_id):
    context = {
        'book': Book.objects.filter(id=book_id).first(),
        'authors': Author.objects.all()
    }
    return render(request, 'book_info.html', context)

def add_auth_to_book(request):
    this_book = Book.objects.get(id=request.POST['book_id'])
    this_book.Authors.add(Author.objects.get(id=request.POST['author']))
    return redirect(f'/books/{request.POST["book_id"]}')

def add_author(request):
    Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes']
    )
    return redirect('/authors/')

def author_data(request, author_id):
    context = {
        'author': Author.objects.filter(id=author_id).first(),
        'books': Book.objects.all()
    }
    return render(request, 'author_info.html', context)

def add_book_to_auth(request):
    this_author = Author.objects.get(id=request.POST['author_id'])
    this_author.books.add(Book.objects.get(id=request.POST['book']))
    return redirect(f'/authors/{request.POST["author_id"]}')