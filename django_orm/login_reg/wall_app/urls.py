from django.urls import path
from . import views, actions

urlpatterns = [
    path('', views.index),
    path('post_message/', actions.create_message),
    path('post_comment/', actions.create_comment),
    path('delete/comment/<int:comment_id>/', actions.delete_comment),
    path('delete/message/<int:message_id>/', actions.delete_message)
]