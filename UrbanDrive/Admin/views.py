from django.shortcuts import render,redirect
from .models import Admin_login
from Cars.models import CarCategory,Car,CarImages,Booking
from Users.models import Users

def admin_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pass")

        try :
            admin = Admin_login.objects.get(email=email)

            if admin.password == password :
                request.session['email'] = admin.email
                return redirect('admin_home')
            else :
                error = "Invalid Email Id or password"
        
        except Admin_login.DoesNotExist:
            error = "Invalid Email Id or password"
        return render(request,"admin/login.html",{'error' : error})
    return render(request,"admin/login.html")

def admin_home(request):
    return render(request,'admin/home.html')

def add_car(request):
    categories = CarCategory.objects.all()

    if request.method == 'POST' :
        brand = request.POST.get('brand')
        name = request.POST.get('name')
        images = request.FILES.getlist('images') 
        category_id = request.POST.get('category')
        year = request.POST.get('year')
        fuel = request.POST.get('fuel')
        gear = request.POST.get('gear')
        average = request.POST.get('average')
        seat = request.POST.get('seat')
        rent = request.POST.get('rent')
        avail = request.POST.get('avail')

        car = Car.objects.create(
            brand=brand,
            name=name,
            category_id=category_id,
            year = year,
            fuel_type = fuel,
            gear_type=gear,
            average = average,
            Seat=seat,
            rent=rent,
            is_avail=avail,
        )

        for image in images :
            CarImages.objects.create(
                car_id = car,
                img = image,
            )

        return redirect("allcar")
    return render(request,'admin/add_car.html',{'categories' : categories})

def allcar(request):
    cars = Car.objects.all()
    return render(request,"admin/allcar.html",{'cars' : cars})

def Update_car(request,id):
    car = Car.objects.get(id=id)
    if request.method == "POST":
        car.brand = request.POST.get('brand')
        car.name = request.POST.get('name')
        category_id = request.POST.get('category')
        car.category = CarCategory.objects.get(id=category_id)
        car.year = request.POST.get('year')
        car.fuel_type = request.POST.get('fuel')
        car.gear_type = request.POST.get('gear')
        car.average = request.POST.get('average')
        car.Seat = request.POST.get('seat')
        car.rent = request.POST.get('rent')
        car.is_avail = request.POST.get('avail') == "True"
        car.start_date = request.POST.get('sd')
        car.start_time = request.POST.get('st')
        car.end_date = request.POST.get('ed')
        car.end_time = request.POST.get('et')

        car.save()

        images = request.FILES.getlist('images')

        if images: 
            CarImages.objects.filter(car_id=car).delete()

            for image in images:
                CarImages.objects.create(car_id=car, img=image)

        return redirect("allcar")
    return render(request,"admin/updatecar.html",
                  {'car' : car ,
                   'categories' : CarCategory.objects.all()})

def Delete_car(request,id):
    car = Car.objects.get(id=id)
    car.delete()
    return redirect('allcar')

def booking(request):
    Booked = Booking.objects.all()
    return render(request,'admin/Bookingdetail.html',{'booked' : Booked})

def user_details(request):
    user = Users.objects.all()
    return render(request,'admin/userdetails.html',{'user' : user})