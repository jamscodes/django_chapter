from django.urls import path
from . import views, actions

urlpatterns = [
    path('', views.index),
    path('add_book/', actions.add_book),
    path('<int:book_id>/', views.book_details),
    path('edit/<int:book_id>/', views.edit_book),
    path('edit_book/<int:book_id>/', actions.edit_book),
    path('favorite/<int:book_id>/', actions.favorite_book),
    path('delete/<int:book_id>', actions.delete_book),
    path('user-dashboard/', views.user_details)
]