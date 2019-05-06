from listApp.models import Property,PropertyImage
import django_filters





class propertyFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(lookup_expr='icontains',label='')

    class Meta:
        model = Property
        fields = ['title','details']


