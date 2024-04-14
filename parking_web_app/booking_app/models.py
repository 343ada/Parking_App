from django.db import models
from registration_app.models import User
from registration_app.models import Vehicle
from registration_app.models import Date_Time

# Create your models here.

class Parking_Lot(models.Model):
    lot_name= models.CharField(max_length=15)
    lot_add1=models.CharField(max_length=15)
    lot_totspace=models.IntegerField
    lot_avaspace=models.IntegerField
    lot_spcnum=models.IntegerField(max_length=2)
    lot_spcstat=models.BooleanField(default=False)
    

    def __str__(self):
        return self.lot_name

class Cost(models.Model):
     cost_confirm=models.IntegerField(unique=True, max_length=6,primary_key=True)
     cost_SpPrice=models.DecimalField(max_digits=4,decimal_places=2)

     def __str__(self):
        return self.cost_confirm



class user(models.Model):
      user=models.ForeignKey(User, on_delete=models.CASCADE)

class date(models.Model):
     date=models.ForeignKey(Date_Time, on_delete=models.CASCADE)

