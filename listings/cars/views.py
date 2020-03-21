from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .filters import CarFilter

# Create your views here.
def home(request):
    #return HttpResponse('Car Listings App')
    cars = Car.objects.all()
    myFilter = CarFilter(request.GET, queryset=cars)
    cars = myFilter.qs
    context = {
        'cars':cars,
        'myFilter': myFilter
    }

    return render(request, 'cars/homepage.html', context)


def report2(request):
    cars = Car.objects.values('brand').annotate(Sum('price'))
    context = {
        'cars': cars,
    }
    return render(request, 'cars/Report2.html', context)
