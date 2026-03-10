from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from .models import Users

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