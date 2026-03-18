from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from .models import Users
from Cars.models import Car
from datetime import datetime

def Register(request) :
    if request.method == "POST" :
        name = request.POST.get("un")
        email = request.POST.get("email")
        password = request.POST.get("pass")

        hased_pass = make_password(password)

        Users.objects.create(
            username=name,
            email=email,
            password = hased_pass
        )
        return redirect("login")
    return render(request,"users/Register.html")

def login(request) :
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pass")

        user = Users.objects.get(email=email)

        if check_password(password,user.password):
            request.session ['username'] = user.username
            request.session ['email'] = user.email 
            return redirect("home")
        else:
            error = "Invalid Email or password!!"
            return render(request,'users/login.html',{'error' : error })

    return render(request,"users/login.html")

def home(request):
    if request.method == 'POST':
        sd = request.POST.get('sd')  
        ed = request.POST.get('ed')  

        print("Start:", sd, "End:", ed)
      
        sd = datetime.strptime(sd, '%Y-%m-%d').date()
        ed = datetime.strptime(ed, '%Y-%m-%d').date()

        available_cars = Car.objects.exclude(
            start_date__lte=ed,  
            end_date__gte=sd     
        )

        return render(request,'cars/cars.html',{'available' : available_cars})

    return render(request,"users/home.html")

def logout(request) :
    request.session.flush()
    return redirect("login")