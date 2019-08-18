from __future__ import unicode_literals
from django.db import models
import re


class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        title_dupe = Shows.objects.get(title=postData['title'])
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Show name should be at least 2 characters"
        if len(postData['description']) < 10:
            errors["description"] = "Show description should be at least 10 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show description should be at least 3 characters"
        if len(postData['release']) < 10:
            errors["release"] = "Show description should be at least 3 characters"
        if postData['title'] == title_dupe.title:
            errors["title"] = "That TV Title is already listed on this site"
        return errors

    def email_validator():    
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(request.form['email']):    # test whether a field matches the pattern            
            errors['email'] = ("Invalid email address!")
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release = models.DateField(auto_now=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager() # add this line!