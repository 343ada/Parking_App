from django.db import models
from registration_app.models import User
from registration_app.models import Vehicle
from registration_app.models import Date_Time
from registration_app.models import Credit_Card
from registration_app.models import Bank
from booking_app.models import Parking_Lot
from booking_app.models import Cost


# Create your models here.

class Pay_User(models.Model):
      pay_user=models.ForeignKey(User, on_delete=models.CASCADE)

class Pay_Date(models.Model):
     pay_date=models.ForeignKey(Date_Time, on_delete=models.CASCADE)

class Pay_Vehicle(models.Model):
      veh=models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class Pay_Card(models.Model):
     card=models.ForeignKey(Credit_Card, on_delete=models.CASCADE)

class Pay_Bank(models.Model):
      bank=models.ForeignKey(Bank, on_delete=models.CASCADE)

class Pay_lot(models.Model):
     lot=models.ForeignKey(Parking_Lot, on_delete=models.CASCADE)

class Pay_Cost(models.Model):
      price=models.ForeignKey(Cost, on_delete=models.CASCADE)





