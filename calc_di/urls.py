#calc_di URL Configuration
#Author Daniel Ilaro da Silva

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('calc_di.core.urls')),
]
