from django.db import models

class Employee(models.Model):
    employee_id=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=255)
    phone=models.CharField(max_length=15)

    def __str__(self):
        return f"{self.employee_id} - {self.name}"



# Create your models here.
