from django.urls import path
from . import views

urlpatterns = [
    path('random_word/', views.generate_rand_string),
    path('reset/', views.reset)
]