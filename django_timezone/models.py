from datetime import datetime
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(default=datetime.now())