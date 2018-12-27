from __future__ import unicode_literals
from django.db import models
import re
NAME_REGEX = re.compile(r'[a-zA-Z]+')
# Create your models here.
class NinjaCheck(models.Manager):
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
        if self.first_name(request) and self.last_name(request):
            return True
        else:
            return False

class Dojo(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length=255)
    desc = models.TextField()
    def __repr__(self):
        return "<Dojo object: {} {} {}>".format(self.name, self.city, self.state)

class Ninja(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    dojo_id = models.ForeignKey(Dojo, related_name="ninjas")
    objects = NinjaCheck()
    def __repr__(self):
        return "<Ninja object: {} {}>".format(self.first_name, self.last_name)
