from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.conf.urls.static import static

# Create your models here.
class Profile(models.Model):
    class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)

        def __str__(self):
            return f'{self.user.username} profile'