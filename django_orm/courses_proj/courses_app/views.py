from django.shortcuts import render, HttpResponse
from .models import Course

# Create your views here.

def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'add_course.html', context)

def delete_course(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
    }
    return render(request, 'delete_course.html', context)

def comment(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
    }
    return render(request, 'course_comments.html', context)