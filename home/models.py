from django.db import models
import templates

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    password=models.CharField(max_length=16)
    message=models.TextField()

