from django.db import models

class Student(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)


class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField()

    def __str__(self):
        return self.car_name


