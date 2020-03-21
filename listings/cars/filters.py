import django_filters
from django_filters import ChoiceFilter, CharFilter

from .models import *

class CarFilter(django_filters.FilterSet):

    # name = django_filters.ModelChoiceFilter(
    #     field_name='name', lookup_expr='isnull',
    #     queryset=Car.objects.all(),
    # )

    # name = ChoiceFilter(field_name='name', choices=STATUS_CHOICES)
    # name = CharFilter(field_name='name', lookup_expr='icontains')
    #name = CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Car
        fields = [
        'name',
        'price',
        'vehicleType',
        'city',
        'country',
        ]

        #fields = '__all__'
        # exclude = [
        #     'power',
        #     'model',
        #     'fuelType',
        #     'brand',
        #     'notRepairedDamage',
        #     'dateCreated'
        # ]
