from django.db import models

# Create your models here.
class Todo(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)
    required_temp = models.IntegerField(default=58)
    zip = models.CharField(max_length=5)
    city = models.CharField(max_length=200, default ="x")
    current_temp = models.IntegerField(default=-1)