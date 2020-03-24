from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('Report2', views.report2),
    path('create', views.createCar, name="create_car"),
    path('update_car/<str:pk>/', views.updateCar, name="update_car"),
    path('delete/<str:pk>/', views.deleteCar, name="delete")
]
