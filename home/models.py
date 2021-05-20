from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    
    description = models.CharField(max_length=150)
    date = models.DateField()

def self (self):
    return self.name