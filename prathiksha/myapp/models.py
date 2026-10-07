from django.db import models
from django.contrib import admin 
class vehiclesevice_DB(models.Model):
    vechicle_no=models.CharField(primary_key=True)
    vehicle_type=models.CharField(max_length=10)
    register_address=models.TextField()
    contact_no=models.IntegerField()
    name=models.CharField(max_length=10)
    email=models.EmailField()
    vehicle_name=models.CharField(max_length=10)
class vehiclesevice_DBAdmin(admin.ModelAdmin):
    list_display=["vechicle_no","vehicle_type","register_address","contact_no","name","email","vehicle_name"]
    