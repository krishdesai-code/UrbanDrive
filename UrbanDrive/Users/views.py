from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from .models import Users
from Cars.models import Car,Booking
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

        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            error = "Invalid Email or password!!"
            return render(request,"users/login.html",{'error': error})

        if check_password(password, user.password):
            request.session['id'] = user.id
            request.session['username'] = user.username
            request.session['email'] = user.email
            request.session.set_expiry(3600)
            return redirect("home")
        else:
            error = "Invalid Email or password!!"
            return render(request,'users/login.html',{'error': error})

    return render(request,"users/login.html")

def home(request):
    if request.method == 'POST':
        sd = request.POST.get('sd')
        st = request.POST.get('st')
        ed = request.POST.get('ed')
        et = request.POST.get('et')

        if not all([sd, st, ed, et]):
            return render(request, "users/home.html", {"error": "Missing date/time"})

        try:
            start_dt = datetime.strptime(sd + " " + st, "%Y-%m-%d %H:%M")
            end_dt = datetime.strptime(ed + " " + et, "%Y-%m-%d %H:%M")
        except ValueError:
            return render(request, "users/home.html", {"error": "Invalid format"})

        if end_dt <= start_dt:
            return render(request, "users/home.html", {"error": "Invalid date/time range"})

        conflicting_bookings = Booking.objects.filter(
            start__lte=end_dt,
            end__gte=start_dt
            )
        booked_car_ids = conflicting_bookings.values_list('car_id', flat=True)
        available_cars = Car.objects.exclude(id__in=booked_car_ids).order_by('-is_avail')
        request.session['start'] = start_dt.isoformat()
        request.session['end'] = end_dt.isoformat()
        return render(request, 'cars/cars.html', {'available': available_cars})
    return render(request, "users/home.html")

def account(request):
    id = request.session.get('id')
    username = request.session.get('username')
    email = request.session.get('email')

    bookingDetails = Booking.objects.filter(user=id).order_by('-id')
    return render(request,'users/account.html',{'username' : username , 'email' : email , 'booking' : bookingDetails})

def logout(request) :
    request.session.flush()
    return redirect("login")