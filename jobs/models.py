from django.db import models

# Create your models here.
class job(models.Model):
    image = models.ImageField(upload_to='images/') #imagefield is same as text field
    summary = models.CharField(max_length=200)# summary for details of job
    #migrate command in cmd is used to make the db know that these are the fields of schema
    

