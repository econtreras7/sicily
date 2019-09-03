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
from .filters import propertyFilter
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext,Template
import json
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render_to_response
#from django.views.generic import DetailView

# Create your views here.


#class propertyList(ListView):
#    template_name = 'listApp/propertyList.html'
#    model = Property


def propertyList(request):
    
    property_list = Property.objects.all()
    property_filter = propertyFilter(request.GET,queryset=property_list)
    return render(request,'listApp/property_list.html',{'filter':property_filter})




    


def home(request):

    featured_list = Property.objects.filter(featured=True)
    if request.method == 'GET':
            form = ContactForm()
            print("GETTTTTTHOME")
    elif request.method == 'POST':

        


        form = ContactForm(request.POST)
        #print(form.cleaned_data['subject'])
        print("POSTHOME")
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            print("home: " + subject +' '+from_email+' '+ message)
            try:
                send_mail(subject, message, from_email, [config('EMAIL_RECIPIENT')])
                
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request,'Success Your Email has been sent!')
    def get_queryset(self):
        query = self.request.GET.get('mainSearch')
        if query:
            results =  Property.objects.filter(title__icontains=query)
            print(results)
            return redirect(request,'listApp/propertylist.html',{'filter':results})

    return render(request,'listApp/home.html',{'featured':featured_list},{'form': form})


def gallery(request):
    return render(request,'listApp/gallery.html')
def process(request):
    return render(request,'listApp/process.html')
    
def aboutSicily(request):
    return render(request, "listApp/aboutSicily.html")
def about(request):
    return render(request, "listApp/about.html")

def contact(request):
    
    if request.method == 'GET':
        form = ContactForm()  
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
          #  name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            print("home: " + subject +' '+from_email+' '+ message)
            try:
                send_mail(subject, message, from_email, [config('EMAIL_RECIPIENT')])
                #messages.success(request,'Success Your Email has been sent!')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request,'Success Your Email has been sent!')#return redirect('success')
    return render(request, "listApp/contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

def contactPopup(request):
    email = request.POST.get("email","")
    subject = request.POST.get("subject","")
    message = request.POST.get("message","")
    print("HEY")
    print("Email"+ email)
    print("Subject"+subject)
    print("Message"+message)
    
    try:
        send_mail(subject, message, email, [config('EMAIL_RECIPIENT')])
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    messages.success(request,'Success Your Email has been sent!')
    return HttpResponse("HEY")
  




def hi(request,name):
     return render(
        request,
        'listApp/hi.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def handler404(request):
    return render(request, 'listApp/404.html',{}, status=404)
def handler500(request):
    return render(request, 'listApp/500.html',{})




    