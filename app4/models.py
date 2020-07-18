from django.db import models
import datetime
class Schedule_New_course(models.Model):
    course=models.CharField(max_length=20,unique=True)
    faculty=models.CharField(max_length=20)
    date=models.DateField(default=datetime.date(2020,1,1))
    time=models.TimeField()
    fee=models.FloatField()
    duration=models.IntegerField()


class StudentModel(models.Model):
    name=models.CharField(max_length=20)
    contactno=models.IntegerField(unique=True)
    email=models.EmailField(max_length=50,unique=True)
    password=models.CharField(max_length=10)


