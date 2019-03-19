import re
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from listApp.models import Property,PropertyImage
from django.views.generic import ListView
#from django.views.generic import DetailView

# Create your views here.


class propertyList(ListView):
    model = Property








def home(request):
    return render(request,'listApp/home.html')



    
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






    