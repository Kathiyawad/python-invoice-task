from django.db import models
from Invoice.models import *

# Create your models here.

class Model_Invoice(models.Model):
    date = models.DateField("Date", auto_now=False, auto_now_add=False)
    customername = models.CharField("Customer Name", max_length=50)

    def __str__(self):
        return self.customername
    

class Model_Invoice_Detail(models.Model):
    invoice = models.ForeignKey(Model_Invoice, on_delete=models.CASCADE, null=True)
    description = models.TextField("Description", max_length=500, null=True, blank=True)
    quantity = models.IntegerField("Quantity", default=True, null=True)
    unitprice = models.IntegerField("Unit Price", default=True, null=True)
    price = models.IntegerField("Price", default=True, null=True)
