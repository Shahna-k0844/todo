from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=200)
    details=models.CharField(max_length=200)
    startdate=models.DateField(max_length=200)
    enddate=models.DateField(max_length=200)
    def __str__(self):
        return self.title
    