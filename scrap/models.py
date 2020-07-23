from django.db import models
from django.conf import settings


class registers(models.Model):
    User_name = models.CharField(max_length=50, default="None")
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.CharField(max_length=10)
    password=models.CharField(max_length=15)
class Document(models.Model):
    Excel_file = models.FileField(upload_to='media')
    ChromePath = models.CharField(max_length=100, default="")
    ColumnName = models.CharField(max_length=100,default="")
    ImagePath = models.CharField(max_length=100,default="")
    No_of_models = models.IntegerField(default=1)



