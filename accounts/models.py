from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    points = models.PositiveIntegerField(default=0)

    def add_points(self, amount):
        self.points += amount
        self.save()