from django.db import models

# Create your models here.


class UF(models.Model):
    date = models.DateField(auto_now=False)
    value = models.DecimalField(max_digits=10, decimal_places=4)

