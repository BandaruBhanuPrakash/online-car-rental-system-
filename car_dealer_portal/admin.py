from django.contrib import admin

# Register your models here. 
from .models import *
admin.site.register(Vehicles)
admin.site.register(Area)
admin.site.register(CarDealer)
