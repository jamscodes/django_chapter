from django.shortcuts import redirect
from .models import Course, Description, Comment
from django.contrib import messages

def add_course(request):
    if request.method == 'POST':
        errors = Course.objects.validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')

        Course.objects.create(
            name = request.POST['name'],
            description = Description.objects.create(desc = request.POST['desc'])
        )
        return redirect('/')
    return redirect('/')

def delete_confirm(request, course_id):
    del_course = Course.objects.get(id=course_id)
    del_course.delete()
    return redirect('/')

def add_comment(request):
    Comment.objects.create(
        comment = request.POST['comment'],
        course = Course.objects.get(id=request.POST['course_id'])
    )
    return redirect(f'/courses/comments/{request.POST["course_id"]}')