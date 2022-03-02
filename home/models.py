from django.db import models

# Create your models here.
class SALES_DATA(models.Model):
    Item_Description  = models.CharField(max_length=50)
    Item_Type =  models.CharField(max_length=30)
    Customer_Name = models.IntegerField()
    Company_Name = models.CharField(max_length=100)
    Amount = models.IntegerField()
    Rate = models.FloatField()
    Status = models.BooleanField()
    Sale_Date = models.DateField()
    Username = models.CharField(max_length=50)
    Address = models.CharField(max_length=150)

class Customer(models.Model):
    Customer_ID  = models.IntegerField()
    Customer_Name = models.CharField(max_length=150)
    Status = models.BooleanField()
    Customer_Type = models.IntegerField()

class Purchase_Data(models.Model):
    Item_Description = models.CharField(max_length=50)
    Item_Type = models.CharField(max_length=30)
    Vendor_Name = models.IntegerField()
    Company_Name = models.CharField(max_length=100)
    Amount = models.IntegerField()
    Rate = models.FloatField()
    Status = models.BooleanField()
    Purchase_Date = models.DateField()
    Username = models.CharField(max_length=50)
    Address = models.CharField(max_length=150)