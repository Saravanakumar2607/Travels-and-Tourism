"""travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tour.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('index/book/', book_trip, name='book_trip'),
    path('booking-success/', booking_success, name='booking_success'),
    #path('index/booking/', booking, name="booking"),
    path('index/register/', register, name='register'),
    path('index/success/', success, name='success'),
] 
