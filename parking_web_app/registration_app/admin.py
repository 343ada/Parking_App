from django.contrib import admin
from .models import User
from .models import Credit_Card
from .models import Bank
from .models import User

admin.site.register(User)
admin.site.register(Credit_Card)
admin.site.register(Bank)

# Register your models here.
