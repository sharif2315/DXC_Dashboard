from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('Report2', views.report2),
    path('create', views.createCar),
]
