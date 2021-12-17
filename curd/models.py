from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=30, blank =False, default="")
    address=models.CharField(max_length=50,blank =False, default="")
    phone=models.IntegerField()
    email=models.EmailField(max_length=30,blank =False, default="")
    def __str__(self):
        return str(self.name)
    
class department(models.Model):
    dept_name = models.CharField(max_length=50, blank =False, default="")
    dept_head=models.CharField(max_length=50,blank =False, default="")
    def __str__(self):
        return str(self.dept_name)

class student(models.Model):
    first_name = models.CharField(max_length=30, blank =False, default="")
    last_name=models.CharField(max_length=50,blank =False, default="")
    departments=models.ForeignKey(department,on_delete=models.CASCADE,related_name='dept_ser', null=True, blank=True)
    def __str__(self):
        return str(self.first_name)
    
