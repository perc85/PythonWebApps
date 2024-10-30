from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Superhero(models.Model):
    name = models.CharField(max_length=100)
    identity = models.CharField(max_length=100)
    description = models.TextField()
    strength = models.CharField(max_length=100)
    weakness = models.CharField(max_length=100)
    image = models.CharField(max_length=100, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name