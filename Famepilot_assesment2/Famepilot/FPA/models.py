from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=50)
    date_of_birth = models.DateField(max_length=10)
    mobile_number = models.CharField(max_length=12)


    def __str__(self):
        return self.name
