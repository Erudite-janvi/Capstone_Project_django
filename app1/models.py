from django.db import models

# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=13,default='',unique=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    password = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.first_name + self.last_name 
