from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('result/', views.form_handler),
    path('form_submitted/', views.form_submission)
]