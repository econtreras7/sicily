import re
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from listApp.models import Property,PropertyImage

# Create your views here.

def home(request):
    #property = Property.objects.get(pk=1)
    #image_list = property.images.all()
    #l = Property.objects.count()
    #for(i in l):
    #allObjects = Property.objects.all()   

    allObjects=1

    #print(l)




    return render(request,"listApp/home.html",{
        'propertyObjects:': allObjects

    }
    
    
    
    
    )
    
def about(request):
    return render(request, "listApp/about.html")

def contact(request):
    return render(request, "listApp/contact.html")

def hi(request,name):
     return render(
        request,
        'listApp/hi.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )






    