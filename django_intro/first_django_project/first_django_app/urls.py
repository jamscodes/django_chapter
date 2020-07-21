from django.urls import path     
from . import views
urlpatterns = [
    path('hello-world/<int:id>', views.index),
    path('another-hello', views.other_index),
    path('hello-world/another-hello', views.a_third), 
]