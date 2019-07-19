from django.db import models

# Create your models here.

class employee(models.Model):
    NAME = models.CharField(max_length = 35)
    DESIGNATION = models.CharField(max_length = 30)
    SALARY = models.BigIntegerField()
    CURRENT = '1'
    RELEAVED = '0'
    STATUS_EMP = [
        (CURRENT, 'Current'),
        (RELEAVED, 'Releaved')
    ]
    STATUS = models.CharField(
        max_length=2,
        choices=STATUS_EMP,
        default=CURRENT,
    )


