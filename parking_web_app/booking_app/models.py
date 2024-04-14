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
    lot_spcnum=models.IntegerField
    lot_spcstat=models.BooleanField(default=False)
    
    def __str__(self):
        return self.lot_name


class Cost(models.Model):
     cost_confirm=models.IntegerField(unique=True, primary_key=True)
     cost_SpPrice=models.DecimalField(max_digits=4,decimal_places=2)

     def __str__(self):
        return self.cost_confirm


class Book_User(models.Model):
      book_user=models.ForeignKey(User, on_delete=models.CASCADE)

class Book_Date(models.Model):
     book_date=models.ForeignKey(Date_Time, on_delete=models.CASCADE)

