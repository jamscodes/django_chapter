from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_money/', views.process_money),
    path('reset/', views.reset),
    path('start_game/', views.start_game),
    path('end_screen/', views.end_screen)
]