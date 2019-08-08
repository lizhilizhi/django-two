from django.db import models

# Create your models here.
from  django.db import models

class Question(models.Model):
    methon = models.CharField(max_length=50)
    path =models.CharField(max_length=200)
    result = models.CharField(max_length=1000)

    def __str__(self):
        return self.methon

class People(models.Model):
    first_name =models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.last_name