from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    customers_id = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=255, null=True, blank=True)
class Usage(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.CharField(max_length=12)
    usage = models.IntegerField()