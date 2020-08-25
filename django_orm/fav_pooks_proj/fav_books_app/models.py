from django.db import models
from login_app.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    added_by = models.ForeignKey(User, related_name="books_added", on_delete=models.CASCADE)
    favorited_by = models.ManyToManyField(User, related_name="favorite_books", default="none")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'Title: {self.title}'
