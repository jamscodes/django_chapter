from django.shortcuts import redirect
from .models import Message, Comment
from login_app.models import User
import logging

logger = logging.getLogger(__name__)

def create_message(request):
    if request.method == 'POST':
        Message.objects.create(
            content = request.POST['message'],
            user = User.objects.get(id=request.POST['user_id'])
        )
    return redirect('/wall/')

def create_comment(request):
    if request.method == 'POST':
        Comment.objects.create(
            content = request.POST['comment'],
            user = User.objects.get(id=request.POST['user_id']),
            message = Message.objects.get(id=request.POST['message_id'])
        )
    return redirect('/wall/')

def delete_comment(request, comment_id):
    del_comment = Comment.objects.get(id=comment_id)
    if request.session['logged_user_id'] == del_comment.user.id:
        del_comment.delete()
    return redirect('/wall/')