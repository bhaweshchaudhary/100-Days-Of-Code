from django.db import models

# Create your models here.
class Header(models.Model):
    head = models.CharField(max_length=100)
    main_text = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    

class SecondSection(models.Model):
    head = models.CharField(max_length=100)