from django.db import models

# Create your models here.
class Picture(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    details=models.TextField()

    def __str__(self):
         return self.name

class Team(models.Model):
    label=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    about=models.TextField()

    def __str__(self):
         return self.label