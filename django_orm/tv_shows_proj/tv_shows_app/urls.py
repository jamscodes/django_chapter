from django.urls import path
from . import views

urlpatterns = [
    path('shows/new/', views.new_show),
    path('shows/<int:show_id>/', views.show_details)
]