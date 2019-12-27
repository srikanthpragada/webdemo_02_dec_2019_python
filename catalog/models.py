from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    mobile = models.CharField(max_length=10, null=True)
    remarks = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name + "," + self.email
