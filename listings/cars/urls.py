from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('Report2', views.report2),
]
