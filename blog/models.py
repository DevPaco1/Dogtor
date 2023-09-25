from django.db import models

# Create your models here.
class Post(models.Model):
    """Model post"""
    name= models.CharField(max_length=50, default="titulo")
    description = models.TextField(max_length=1000, blank=True, null=True)

def __str__(self):
    return f"{self.pk}: {self.name}"