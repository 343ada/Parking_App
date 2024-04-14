from django.db import models
from registration_app.models import User

# Create your models here.
class Aut_user(models.Model):
    
    aut_user=models.ForeignKey(User, on_delete=models.CASCADE)
