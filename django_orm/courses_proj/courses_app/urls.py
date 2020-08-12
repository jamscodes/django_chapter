from django.urls import path
from . import views, actions

urlpatterns = [
    path('', views.index),
    path('add_course/', actions.add_course),
    path('courses/delete/<int:course_id>/', views.delete_course),
    path('courses/delete/<int:course_id>/confirm/', actions.delete_confirm),
    path('courses/comments/<int:course_id>/', views.comment),
    path('add_comment/', actions.add_comment)
]