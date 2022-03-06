from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100, default=None, null=True)
    last_name = models.CharField(max_length=100, default=None, null=True)
    email = models.EmailField(max_length=100, default=None, null=True)
    gender = models.CharField(max_length=1, default=None, null=True)
    date_of_birth = models.DateField(default=None, null=True)
    industry = models.CharField(max_length=100, default=None, null=True)
    salary = models.DecimalField(default=None, null=True, decimal_places=2, max_digits=12)
    years_of_experience = models.IntegerField(default=None, null=True)