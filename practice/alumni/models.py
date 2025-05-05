from django.db import models

# Create your models here.
class Alumni(models.Model):
    name = models.CharField(max_length=100,default="null")
    title = models.CharField(max_length=255,default="null")
    graduation_year = models.IntegerField(default=0)
    department = models.CharField(max_length=255,default="Department of Computer Science and Engineering")
    university = models.CharField(max_length=255,default="University of Asia Pacific")
    bio = models.TextField(max_length=3000,default="null")
    photo = models.ImageField(upload_to='alumni_photos/',default='media/img.png')
    def __str__(self):
        return self.name
