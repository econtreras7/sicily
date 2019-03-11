import re
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from listApp.models import Property,PropertyImage
from django.views.generic import ListView

# Create your views here.


class propertyList(ListView):
    model = Property




def home(request):
    property = Property.objects.get(pk=1)
    image_list = property.images.all()
    l = Property.objects.count()
    #for(i in l):
    propertyObjects = Property.objects.all()   
   # Property.ob
    #allObjects=1

    print(l)
    print(propertyObjects[1].title)



    return render(request,'listApp/home.html',{
        'propertyObjects:': propertyObjects

    })



    
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






    