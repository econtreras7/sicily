from django.contrib import admin
from django.db import models
from listApp.models import Property
from listApp.models import PropertyImage

# Register your models here.
class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 3

class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline, ]

admin.site.register(Property,PropertyAdmin)