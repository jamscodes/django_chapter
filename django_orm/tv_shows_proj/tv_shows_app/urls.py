from django.urls import path
from . import views, actions

urlpatterns = [
    path('shows/', views.shows),
    path('shows/new/', views.new_show),
    path('shows/<int:show_id>/', views.show_details),
    path('shows/<int:show_id>/edit/', views.edit_show),
    path('add_show/', actions.add_show),
    path('edit_show/', actions.edit_show)
]