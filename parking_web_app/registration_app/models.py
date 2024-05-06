from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_fname= models.CharField(max_length=15)
    user_lname= models.CharField(max_length=20)
    username= models.CharField(max_length=20)
    user_add1 = models.CharField(max_length=20)
    user_add2 = models.CharField(max_length=20)
    user_city = models.CharField(max_length=20)
    user_state = models.CharField(max_length=20)
    user_zip = models.CharField(max_length=5)
    user_email = models.EmailField(default = 'sombody@email.com')
    user_password = models.CharField(max_length=20)
    
    def set_password(self, raw_password):
        self.user_password = make_password(raw_password)

    
    def __str__(self):
        return self.username


class Credit_Card(models.Model):
    card_fname = models.CharField(max_length=15)
    card_lname = models.CharField(max_length=20)
    card_add1 = models.CharField(max_length=20)
    card_add2 = models.CharField(max_length=20)
    card_city = models.CharField(max_length=20)
    card_state = models.CharField(max_length=20)
    card_zip = models.CharField(max_length=2)
    card_number= models.IntegerField(primary_key=True)
    card_SecNum= models.IntegerField()
    card_ExpDate= models.DateField(max_length=4)

    def __str__(self):
        return f"{self.card_fname} {self.card_lname}" 
    
class Bank(models.Model):
    bank_name= models.CharField(max_length=15)
    bank_add1=models.CharField(max_length=20)
    bank_add2=models.CharField(max_length=20)
    bank_city=models.CharField(max_length=15)
    bank_state=models.CharField(max_length=2)
    bank_zip=models.CharField(max_length=5)
    bank_acctnum=models.IntegerField(primary_key=True)
    bank_routnum= models.CharField(max_length=9)

    def __str__(self):
        return self.bank_name
    
class Vehicle (models.Model):
    veh_year=models.IntegerField()
    veh_make=models.CharField(max_length=12)
    veh_model=models.CharField(max_length=15)
    veh_color=models.CharField(max_length=10)
    veh_licnum=models.CharField(max_length=7)
    veh_vin=models.CharField(max_length=17,primary_key=True)
    
    def __str__(self):
        return self.veh_make
    
class Date_Time(models.Model):
    date = models.DateField
    datetime=models.DateTimeField
    time=models.TimeField

    def __str__(self):
        return self.date
    
