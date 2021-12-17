from django.db import models

# Create your models here.


class student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def __str__(self):
        return self.first_name


class department(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_head = models.CharField(max_length=100)
    depart = models.ForeignKey(student, on_delete=models.CASCADE, related_name='departments', null=True, blank=True)
    def __str__(self):
        return self.first_name