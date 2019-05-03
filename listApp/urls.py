from django.urls import path
from listApp import views
from django.contrib import admin
from listApp.views import propertyList
from listApp.views import home
from django.conf.urls import url
urlpatterns = [
    path("", views.home, name="home"),
    path("home/",views.home,name ="home"),
    path("hello/<name>", views.hi,name="hi"),
    path("Hello/<name>", views.hi, name="hi"),
    #path("properties/",propertyList.as_view()),
    path("about/", views.about,name="about"),
    path("contact/", views.contact,name="contact"),
    path("success/", views.successView,name="success"),
    path("gallery/", views.gallery,name="gallery"),
    path("process/", views.process,name="process"),
    path("aboutSicily/", views.aboutSicily,name="aboutSicily"),
     url(r'^propertyList/$', views.propertyList, name='propertyList'),
]