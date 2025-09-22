# Ex02 Django ORM Web Application
# Date:22-09-2025
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).


## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM
```
admin.py

from django.contrib import admin
from .models import CarInventory,CarInventoryadmin
admin.site.register(CarInventory,CarInventoryadmin)


models.py

from django.db import models
from django.contrib import admin



class CarInventory(models.Model):
    carno=models.IntegerField(primary_key=True)
    carname=models.CharField(max_length=100)
    carowner=models.CharField(max_length=100)
    carowner_phoneno=models.IntegerField()
    price_in_rupees=models.IntegerField()
    
class CarInventoryadmin(admin.ModelAdmin):
    list_display=('carno','carname','carowner','carowner_phoneno','price_in_rupees')
    
```
# OUTPUT
![alt text](<Screenshot (9).png>)



# RESULT
Thus the program for creating a database using ORM hass been executed successfully
