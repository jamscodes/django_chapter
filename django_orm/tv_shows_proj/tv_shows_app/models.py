from django.db import models
import datetime

# Create your models here.

class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        cur_date = datetime.datetime.today()
        post_date = postData.get('rel_date')
        if len(Movie.objects.filter(title=postData["title"])) > 0:
            errors['unique'] = 'This show already exists' # this is put in for a bonus goal and it's dumb because it doesn't allow you to edit a show without changing the title
        if len(postData['title']) < 2:
            errors['title'] = 'Title should be at least 2 characters'
        if len(postData['network']) < 3:
            errors['network'] = 'Network should be at least 3 characters'
        if len(post_date) < 1:
            errors['rel_date'] = 'Release date should be a full date'
        if 'rel_date' not in errors and datetime.datetime.strptime(post_date, "%Y-%m-%d") >= cur_date:
            errors['past_date'] = 'Release date should be in the past'
        if len(postData['desc']) > 0 and len(postData['desc']) <= 10:
            errors['desc'] = 'Description should be at least 10 characters.'
        return errors

class Movie(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()