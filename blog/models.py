from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=255)
    pubdate = models.DateField()
    body  = models.TextField()
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')