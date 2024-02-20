from django.db import models

# Create your models here.
class First_Model (models.Model):
    title = models.CharField(max_length = 200)