from django.db import models
from registration_app.models import User
from registration_app.models import Vehicle
from registration_app.models import Date_Time
from django.contrib.auth.models import User

# Create your models here.

class Parking_Lot(models.Model):
    lot_name= models.CharField(max_length=15)
    lot_add1=models.CharField(max_length=15)
    lot_totspace=models.IntegerField(default=100)
    lot_avaspace=models.IntegerField(default=100)
    lot_spcnum=models.IntegerField
    lot_spcstat=models.BooleanField(default=True)
    

    
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


class ParkingReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parking_lot = models.ForeignKey(Parking_Lot, on_delete=models.CASCADE, null=True)  # Add ForeignKey to Parking_Lot
    parking_spot = models.CharField(max_length=100)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        # Update the parking lot space status if available space becomes zero
        if self.parking_lot.lot_avaspace <= 0:
            self.parking_lot.lot_spcstat = False
            self.parking_lot.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reservation for {self.user.username} at {self.parking_spot}"