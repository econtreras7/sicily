from listApp.models import Property,PropertyImage
import django_filters





class propertyFilter(django_filters.FilterSet):

    reference = django_filters.CharFilter(lookup_expr='icontains',label='')

    class Meta:
        model = Property
        fields = ['reference','details']


