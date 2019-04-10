from django.db import models

# Create your models here.




class Property(models.Model):
    title = models.TextField(default='Title')
    details = models.TextField(default='Details')
    mainDetails =models.TextField(default='Main Details')
    reference = models.TextField(default='Reference')
    price = models.IntegerField(default=0)
    propertyType = models.TextField(default='Property Type')
    status= models.TextField(default='Status')
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    sqft = models.IntegerField(default=0)
    facebookLink = models.TextField(default='Facebook Link')
    propertyYoutube = models.TextField(default='YouTube Link')
    address = models.TextField(default='Address')

    def __str__(self):
       return self.title

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images',on_delete=models.CASCADE)
    image = models.ImageField()
    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.url()) )
    image_tag.short_description = 'Image'