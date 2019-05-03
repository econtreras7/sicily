from django.db import models
from django.core.exceptions import ValidationError
from djmoney.models.fields import MoneyField
from djmoney.contrib.exchange.models import convert_money
# Create your models here.

def validate_only_3_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 3 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)

PROPERTY_STATUS =(
    ('FOR SALE','For Sale'),
    ('FOR RENT','Pending Sale'),
    ('SOLD','Sold'),
)
class Property(models.Model):
    
    title = models.CharField(max_length=20,default='Title')
    propertyStatus=models.CharField(max_length=10,choices=PROPERTY_STATUS,default='FOR SALE')
    details = models.TextField(default='Details')
    mainDetails =models.TextField(default='Main Details')
    reference = models.CharField(max_length=10,default='Reference')
    price = MoneyField(decimal_places=0,max_digits=10,default=0,default_currency='EUR')
    propertyType = models.CharField(max_length=10,default='Property Type')
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    sqmt = models.IntegerField(default=0)
    facebookLink = models.TextField(default='Facebook Link')
    propertyYoutube = models.TextField(default='YouTube Link')
    address = models.TextField(default='Address')
    featured = models.BooleanField(default=False)
    def __str__(self):
       return self.title

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images',on_delete=models.CASCADE)
    image = models.ImageField()
    


class featuredProperties(models.Model):
        Property
