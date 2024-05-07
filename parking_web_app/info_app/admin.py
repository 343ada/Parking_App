from django.contrib import admin
from .models import CreditCard
from .models import Bank
from .models import Vehicle

admin.site.register(CreditCard)
admin.site.register(Bank)
admin.site.register(Vehicle)

# Register your models here.
