from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_dojo/', views.add_dojo, name='add_dojo'),
    path('add_ninja/', views.add_ninja)
]