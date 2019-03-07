from django.db import models

# Create your models here.




class Property(models.Model):
    address = models.TextField()



class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images',on_delete=models.CASCADE)
    image = models.ImageField()



