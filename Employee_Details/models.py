from tabnanny import check
from django.db import models

class Department(models.Model):
    D_Name = models.CharField(max_length=100,default=None)
    D_location = models.CharField(max_length=100)

    def __str__(self) :
        return self.D_Name

class Role(models.Model):
    R_Name = models.CharField(max_length=100,default=None)

    def __str__(self) :
        return self.R_Name

class Employee(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField()
    dept=models.ForeignKey(Department, on_delete=models.CASCADE)
    Salary = models.IntegerField(default=" ")
    Bonus = models.IntegerField(default='')
    Role = models.ForeignKey(Role, on_delete=models.CASCADE)
    Phone = models.IntegerField(default='')
    Hire_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return "%s %s %s" %(self.First_Name,self.Last_Name,self.Email)

