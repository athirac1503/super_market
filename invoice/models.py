from tkinter import CASCADE
from django.db import models


# Create your models here.
class CustomerReg(models.Model):
    phone=models.BigIntegerField()
    name=models.CharField(max_length=50)
    date=models.CharField(max_length=50,null=True)
    invoice_no=models.BigIntegerField(null=True)

    class Meta:
        db_table='customer_reg'
class Master(models.Model):
    item_code=models.BigIntegerField(null=True)
    item_name=models.CharField(max_length=40)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    stock=models.BigIntegerField(null=True)
    
    class Meta:
        db_table="item_master"

class Customer(models.Model):
    phone=models.BigIntegerField()
    name=models.CharField(max_length=40)
    date=models.CharField(max_length=50)
    invoice_no=models.BigIntegerField()
    item_name=models.CharField(max_length=50,null=True)
    quantity=models.BigIntegerField(null=True)
    unit=models.BigIntegerField(null=True)
    product_id=models.ForeignKey(Master,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table='customer'

