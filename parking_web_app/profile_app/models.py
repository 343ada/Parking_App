from django.db import models
from registration_app.models import User
from registration_app.models import Vehicle
from registration_app.models import Date_Time
from registration_app.models import Credit_Card
from registration_app.models import Bank
from booking_app.models import Parking_Lot
from booking_app.models import Cost

# Create your models here.
class User(models.Model):
      user=models.ForeignKey(User, on_delete=models.CASCADE)

class Date(models.Model):
     date=models.ForeignKey(Date_Time, on_delete=models.CASCADE)

class Vehicle(models.Model):
      user=models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class Creditcard(models.Model):
     date=models.ForeignKey(Credit_Card, on_delete=models.CASCADE)

class Bank(models.Model):
      user=models.ForeignKey(Bank, on_delete=models.CASCADE)

class Parklot(models.Model):
     date=models.ForeignKey(Parking_Lot, on_delete=models.CASCADE)

class Cost(models.Model):
      user=models.ForeignKey(Cost, on_delete=models.CASCADE)