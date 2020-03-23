from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *
from .filters import CarFilter, report2Filter

# Create your views here.
def home(request):
    #return HttpResponse('Car Listings App')
    cars = Car.objects.all()

    form = CarForm()

    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


    # myFilter = CarFilter(request.GET, queryset=cars)
    # cars = myFilter.qs
    context = {
        'cars':cars,
        'form': form,
        # 'myFilter': myFilter,
    }

    return render(request, 'cars/homepage.html', context)


def report2(request):
    cars = Car.objects.values('brand').annotate(Sum('price'))
    myFilter = report2Filter(request.GET, queryset=cars)
    cars = myFilter.qs
    context = {
        'cars': cars,
        'myFilter': myFilter,
    }
    return render(request, 'cars/Report2.html', context)

def createCar(request):
    form = CarForm()
    context = { 'form': form }
    return render(request, 'cars/create.html', context)
