from django.db import models

# Create your models here.




class Property(models.Model):
    title = models.TextField(default='Title')
    details = models.TextField(default='details')
    mainDetails =models.TextField(default='Main Details')
    reference = models.TextField(default='Reference')
    price = models.IntegerField(default=0)
    propertyType = models.TextField(default='Property Type')
    status= models.TextField(default='Status')
    bedrooms = models.IntegerField(default=0)
    propertyYoutube = models.TextField(default='YouTube Link')
    address = models.TextField(default='Address')



class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images',on_delete=models.CASCADE)
    image = models.ImageField()



