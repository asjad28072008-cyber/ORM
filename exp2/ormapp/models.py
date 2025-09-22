from django.db import models
from django.contrib import admin

# Create your models here.

class CarInventory(models.Model):
    carno=models.IntegerField(primary_key=True)
    carname=models.CharField(max_length=100)
    carowner=models.CharField(max_length=100)
    carowner_phoneno=models.IntegerField()
    price_in_rupees=models.IntegerField()
    
class CarInventoryadmin(admin.ModelAdmin):
    list_display=('carno','carname','carowner','carowner_phoneno','price_in_rupees')
    