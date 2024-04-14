from django.db import models
from registration_app.models import User

# Create your models here.
class user(models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE)
