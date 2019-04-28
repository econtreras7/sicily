import re
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.shortcuts import render, redirect
from listApp.models import Property,PropertyImage
from django.views.generic import ListView
#from collection.forms import ContactForm
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from decouple import config
#from django.views.generic import DetailView

# Create your views here.


class propertyList(ListView):
    model = Property
    


def home(request):
    featured_list = Property.objects.all()


    return render(request,'listApp/home.html',{'featured':featured_list})


def gallery(request):
    return render(request,'listApp/gallery.html')
def acquisition(request):
    return render(request,'listApp/acquisition.html')
    
def about(request):
    return render(request, "listApp/about.html")

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [config('EMAIL_RECIPIENT')])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request,'Success Your Email has been sent!')
            #return HttpResponseRedirect('')
    return render(request, "listApp/contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')




    

def hi(request,name):
     return render(
        request,
        'listApp/hi.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )






    