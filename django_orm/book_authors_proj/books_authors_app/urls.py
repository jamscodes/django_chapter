from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books/', views.books),
    path('add_book/', views.add_book),
    path('books/<int:book_id>', views.book_data),
    path('add_auth_to_book/', views.add_auth_to_book),
    path('authors/', views.authors),
    path('add_author/', views.add_author),
    path('authors/<int:author_id>', views.author_data),
    path('add_book_to_auth/', views.add_book_to_auth)
]