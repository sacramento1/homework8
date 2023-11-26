from django.db import models
from django.contrib.auth.models import User
from django.forms import forms
from userprofile.models import UserProfile


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250, default='sometitle')
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return self.title

class Media(models.Model):
    owner = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(default='bek.png')

    def __str__(self) -> str:
        name = str(self.image)
        return name[:-4]
