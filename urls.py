"""
URL configuration for car_rental_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home,),
    path("home",views.home,),
    path("cars",views.cars,),
    path("about",views.about,),
    path("register",views.register,name="Register"),
    path("login",views.login,name="Login"),
    path("reg",views.reg),
    path("log",views.log), 
    path("booking",views.booking,name="Booking"), 
    path("confirm",views.confirm,name="Confirm"), 
    path("confirmation",views.confirmation,name="Confirmation"),         
]
