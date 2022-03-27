from django.db import models

# Create your models here.
class Footer(models.Model):
    footer_text = models.CharField(max_length=50)

    def __str__(self):
        return self.footer_text