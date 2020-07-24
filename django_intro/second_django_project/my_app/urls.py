from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:blog_id>/', views.show),
    path('edit/<int:blog_id>/', views.edit),
    path('<int:blog_id>/delete/', views.delete),
    path('linked-page.html/', views.linked_page),
    path('display-values.html/', views.display_values)
]