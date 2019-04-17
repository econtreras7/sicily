from listApp.models import Property,PropertyImage
import django_filters





class ListFilter():
    class Meta:
        model = Property
        fields = []


