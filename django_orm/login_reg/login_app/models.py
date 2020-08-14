from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def reg_validation(self, postData):
        errors = {}

        NAME_REGEX = re.compile(r'[a-zA-Z][a-zA-Z]+')
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not NAME_REGEX.match(postData['f_name']):
            errors['f_name'] = 'First name must only contain letters and be at least 2 characters'
        if not NAME_REGEX.match(postData['l_name']):
            errors['l_name'] = 'Last name must only contain letters and be at least 2 characters'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Email address is invalid'
        if len(postData['pw']) < 8:
            errors['pw'] = 'Password should be at least 8 characters in length'
        if postData['pw'] != postData['conf_pw']:
            errors['conf_pw'] = 'Passwords do not match.'
        
        return errors

class User(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return f'User: {self.f_name} {self.l_name}'