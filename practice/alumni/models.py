from django.db import models

# Create your models here.
class Alumni(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(max_length=100)
    designation = models.CharField(max_length=100)
    classYear = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    otherContacts = models.TextField(default='')
    message = models.TextField(max_length=1000)
    def __str__(self):
        return self.name