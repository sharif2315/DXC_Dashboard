from django.db import models
from django.db.models import Avg, Min, Max, Sum, Count
# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.IntegerField()
    vehicleType = models.CharField(max_length=50, null=True)
    yearOfRegistration = models.IntegerField()
    gearBox = models.CharField(max_length=6, null=True)
    power = models.IntegerField()
    model = models.CharField(max_length=50, null=True)
    mileage = models.IntegerField()
    fuelType = models.CharField(max_length=50, null=True)
    brand = models.CharField(max_length=50)
    notRepairedDamage = models.CharField(max_length=3, null=True)
    dateCreated = models.DateField()
    city = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

#sqlQuery = select sum(price), brand, city from listings.cars_car group by brand, city;
#pythonQuery = Car.objects.values('brand', 'city').annotate(Sum('price'))

# class Dealer(models.Model):
#     name = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)
#     area = models.CharField(max_length=50, null=True)
