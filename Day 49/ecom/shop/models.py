from email.policy import default
from django.db import models 

# Create your models here.
class Footer(models.Model):
    footer_text = models.CharField(max_length=50)

    def __str__(self):
        return self.footer_text

class Testimonial(models.Model):
    user_name = models.CharField(max_length=50)
    review = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.user_name

class Telephone(models.Model):
    number = models.CharField(max_length=12)

    def __str__(self):
        return self.number
