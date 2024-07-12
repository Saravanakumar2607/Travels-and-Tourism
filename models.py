from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CustomUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
    
class Booking(models.Model):
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    persons = models.PositiveIntegerField()
    arrival_date = models.DateField()
    leaving_date = models.DateField()
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return  self.from_location
    
 
