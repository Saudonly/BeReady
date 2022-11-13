from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Creating a Human Resource profile for the user
class HumanResourceProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    field = models.CharField(max_length=64)
    desceiption = models.TextField()
    image = models.ImageField(upload_to="images/")



