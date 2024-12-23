from django.urls import path
from . import views

urlpatterns = [
    path('', views.unit_converter, name='unit_converter'),
]
