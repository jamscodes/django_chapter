from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_time),
    path('time-display/', views.display_time)
]