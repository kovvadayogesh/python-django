from django.db import models

# Create your models here.


class Employee(models.Model):
    employee_name = models.CharField(max_length=10)

    def __str__(self):
        return self.employee_name
    

class EmployeeDetails(models.Model):
    employee = models.OneToOneField(Employee,on_delete=models.CASCADE)
    employee_email = models.EmailField()
    employee_phone = models.IntegerField()

    def __str__(self):
        return self.employee_email