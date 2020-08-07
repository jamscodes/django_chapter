from django.db import models

# Create your models here.

class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = 'Title should be at least 2 characters'
        if len(postData['network']) < 2:
            errors['network'] = 'Network should be at least 2 characters'
        if len(postData.get('rel_date')) < 2:
            errors['rel_date'] = 'Please input full release date'
        if len(postData['desc']) < 2:
            errors['desc'] = 'Description should be at least 2 characters'
        return errors

class Movie(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()