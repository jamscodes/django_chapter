from django.shortcuts import redirect
from .models import Book
from login_app.models import User

def add_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title = request.POST['b_title'],
            desc = request.POST['b_desc'],
            added_by = User.objects.get(id = request.session['logged_user_id'])
        )
        book = Book.objects.get(title = request.POST['b_title'])
        book.favorited_by.add(User.objects.get(id=request.session['logged_user_id']))
    return redirect('/books/')

def edit_book(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(id=book_id)
        book.title = request.POST['b_title']
        book.desc = request.POST['b_desc']
        book.save()
    return redirect(f'/books/edit/{book_id}/')

def favorite_book(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['logged_user_id'])
    if user not in book.favorited_by.all():
        book.favorited_by.add(user)
        book.save()
    else:
        book.favorited_by.remove(user)
        book.save()
    return redirect('/books/')

def delete_book(request, book_id):
    if 'logged_user_id' in request.session and request.session['logged_user_id'] == Book.objects.get(id=book_id).added_by.id:
        del_book = Book.objects.get(id=book_id)
        del_book.delete()
    return redirect('/books/')
