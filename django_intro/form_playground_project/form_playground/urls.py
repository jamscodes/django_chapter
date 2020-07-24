from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('result/', views.form_handler, name='handler'),
    path('form_submitted/', views.form_submission)
]