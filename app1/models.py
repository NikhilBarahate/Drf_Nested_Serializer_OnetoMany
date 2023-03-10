from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    sal = models.FloatField()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='emp_project')

    def __str__(self):
        return self.name