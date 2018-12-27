from __future__ import unicode_literals
from django.db import models
import re
NAME_REGEX = re.compile(r'[a-zA-Z]+')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class AuthorCheck(models.Manager):
    def email(self, request):
        if 'email' not in request.POST:
            return False
        if len(request.POST['email'])<1:
            return False
        elif not EMAIL_REGEX.match(request.POST['email']):
            return False
        else:
            return True
    def first_name(self, request):
        if 'first_name' not in request.POST:
            return False
        elif len(request.POST['first_name']) < 2:
            return False
        elif not NAME_REGEX.match(request.POST["first_name"]):
            return False
        else:
            return True
    def last_name(self, request):
        if 'last_name' not in request.POST:
            return False
        elif len(request.POST['last_name'])<2:
            return False
        elif not NAME_REGEX.match(request.POST['last_name']):
            return False
        else:
            return True
    def valid_user(self, request):
        if self.email(request) and self.first_name(request) and self.last_name(request):
            return True
        else:
            return False

class Book(models.Model):
    title = models.CharField(max_length = 255)
    desc = models.TextField()
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Book object: {} {}>".format(self.title, self.desc)

class Author(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorCheck()
    def __repr__(self):
        return "<Author object: {} {} {} {}>".format(self.first_name, self.last_name, self.email, self.books)
