from django.shortcuts import render,redirect
from pathlib import Path
import os
from .models import Register,Confirm
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required

#from django.contrib.auth.models import User
BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.
def home(request):
    result = os.path.join(BASE_DIR,"templates")
    print(result)
    return render(request,"home.html")
def cars(request):
    return render(request,"car.html")
def about(request):
    return render(request,"about.html")
def register(request):
    return render(request,"register.html")
def login(request):
    return render(request,"login.html")
def booking(request):
    return render(request,"booking.html")
def reg(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmpassword = request.POST["confirmPassword"]
        phone=request.POST["phone"]

        if password == confirmpassword:
            registration = Register(name=name,email=email,password=password,confirmpassword=confirmpassword,phone=phone)
            registration.save()
            messages.success(request, 'You are registered successfully.')
            return redirect("Login")
        else:
            messages.warning(request, 'Password do not match')
            return redirect("Register")
    else:
        return render(request, "register.html")
def log(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        registrtion = auth.authenticate(Register(request,email=email, password=password))

        if registrtion is not None:
            login(request,registrtion )
            messages.success(request, 'You are now logged in.')
            return redirect('Booking')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('Booking')
    #return render(request, 'login.html')
def confirm(request):
        if request.method == "POST":
            pickupLocation= request.POST["pickupLocation"]
            dropoffLocation= request.POST["dropoffLocation"]
            pickupDate= request.POST["pickupDate"]
            dropoffdate= request.POST["dropoffDate"]
            cartype=request.POST["cartype"]
            #con= Confirm(pickupLocation=pickupLocation,dropoffLocation=dropoffLocation,pickupDate=pickupDate,dropoffdate=dropoffdate,cartype=cartype)
            #con.save()
            return redirect('Confirmation')
        else:
            return render(request, "booking.html")
def confirmation(request):
    return render(request,"confirm.html")
    





