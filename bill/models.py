from django.db import models

# Create your models here.
class Vendor(models.Model):
    name=models.CharField(max_length=40)
    date=models.CharField(max_length=40)
    bill_no=models.BigIntegerField()

    class Meta:
        db_table='vendor'