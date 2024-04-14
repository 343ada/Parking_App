from django.db import models
from registration_app.models import User
from registration_app.models import Vehicle
from registration_app.models import Date_Time
from registration_app.models import Credit_Card
from registration_app.models import Bank
from booking_app.models import Parking_Lot
from booking_app.models import Cost

# Create your models here.
class Pro_User(models.Model):
     pro_user=models.ForeignKey(User, on_delete=models.CASCADE)

class Pro_Date(models.Model):
     pro_date=models.ForeignKey(Date_Time, on_delete=models.CASCADE)

class Pro_Vehicle(models.Model):
      pro_veh=models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class Pro_Card(models.Model):
     pro_card=models.ForeignKey(Credit_Card, on_delete=models.CASCADE)

class Pro_Bank(models.Model):
    pro_bank=models.ForeignKey(Bank, on_delete=models.CASCADE)

class Pro_lot(models.Model):
     pro_lot=models.ForeignKey(Parking_Lot, on_delete=models.CASCADE)

class Pro_Cost(models.Model):
      pro_cost=models.ForeignKey(Cost, on_delete=models.CASCADE)