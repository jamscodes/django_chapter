from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __repr__(self):
        return "Title: {}".format(self.title)

class Actor(models.Model):
    f_name = models.CharField(max_length=45)
    l_name = models.CharField(max_length=45)
    movies = models.ManyToManyField(Movie, related_name="actors")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __repr__(self):
        return f"Name: {self.f_name} {self.l_name}"