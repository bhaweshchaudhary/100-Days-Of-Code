from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.EmailField(primary_key=True, max_length=50)
    message = models.TextField(max_length=200)