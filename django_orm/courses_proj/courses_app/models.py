from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}

        if len(postData['name']) <= 5:
            errors['name'] = 'Course name should be longer than 5 characters long'
        if len(postData['desc']) <= 15:
            errors['desc'] = 'Course description should be longer than 15 characters long'

        return errors

class Description(models.Model):
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField(Description, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # comments = Comment.objects.filter(id=Course.id)
    objects = CourseManager()

    def __repr__(self):
        return f'Course: {self.name}'

class Comment(models.Model):
    comment = models.TextField()
    course = models.ForeignKey(Course, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
