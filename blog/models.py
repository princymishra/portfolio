from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=255)
    pubdate = models.DateField()
    body  = models.TextField()
    image = models.ImageField(upload_to = 'images/')