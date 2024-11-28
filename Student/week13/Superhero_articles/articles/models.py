from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Investigator(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Superhero(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    identity = models.CharField(max_length=100)
    description = models.TextField()
    strength = models.CharField(max_length=100)
    weakness = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)
    
    def delete(self, *args, **kwargs):
        if self.is_default:
            raise ValueError("Default heroes cannot be deleted.")
        super().delete(*args, **kwargs)

class SuperheroImage(models.Model):
    superhero = models.ForeignKey(Superhero, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='superheroes/')
