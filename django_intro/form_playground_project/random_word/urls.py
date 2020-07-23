from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_rand_string),
    path('reset/', views.reset)
]