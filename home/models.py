
from django.db import models

# Create your models here.

class Student(models.Model):
    # id=models.AutoField()
    name=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()
    address=models.TextField(null=True,blank=True)



class car(models.Model):
    name = models.CharField(max_length=100)
    speed = models.IntegerField()

    def __str__(self) -> str:
        return (f'{self.id}:the name of car is {self.name} and its speed is {self.speed}')
