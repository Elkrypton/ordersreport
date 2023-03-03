from django.db import models
import pyqrcode
# Create your models here.
from django.db import models

class Manufacturer(models.Model):
    vendor = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    store_sku = models.CharField(max_length=50)
    omsid = models.CharField(max_length=50)
    store_so_sku = models.CharField(max_length=50)
    parts_usage = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)


