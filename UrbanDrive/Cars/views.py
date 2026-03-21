from django.shortcuts import render,redirect
from .models import Car,Booking
from Users.models import Users
from django.utils import timezone
from .decorators import session_login_required

def cars(request):
    return render(request,'cars/cars.html')

def car_detail(request,id):
    car = Car.objects.get(id=id)
    return render(request,'cars/car_detail.html',{'car' : car})

@session_login_required
def booking_form(request,id):

    user_id = request.session.get('id')
    car = Car.objects.get(id=id)
    booked = None
    
    if user_id:
       user = Users.objects.get(id=user_id)
    else :
        return redirect("login")

    if request.method == "POST":
        aadhar = request.POST.get("aadhar")
        dob = request.POST.get("dob")
        licence = request.POST.get("licence")
        exp = request.POST.get("valid")
        phoneNum = request.POST.get("mn")

        current_time = timezone.now().strftime("%Y%m%d%H%M%S")
        id = "BD" + aadhar.replace(" ", "")[8:] + phoneNum.replace(" ", "")[6:] + current_time

        start_dt = request.session.get('start')
        end_dt = request.session.get('end')

        booked = Booking.objects.create(
            id = id,
            user=user,
            car=car,
            aadhar=aadhar,
            aadhar_dob=dob,
            licence=licence,
            licence_exp=exp,
            mobile_no=phoneNum,
            rent=car.rent,
            start=start_dt,
            end = end_dt,
        )
        booked.save()
        request.session.flush()
        return redirect("confirm_booking",booking_id=booked.id)
    return render(request,'cars/bookingform.html',{'booking' : booked})

def confirm_booking(request,booking_id):
    request.session ["BI"] = booking_id
    booking_car = Booking.objects.get(id=booking_id)
    car = Car.objects.get(id=booking_car.car.id)
    return render(request,'cars/confirm_booking.html',
    {'book' : booking_car ,
      'car' : car })

def car_booked(request):
    bookingId = request.session.get('BI')
    username = request.session.get('username')
    return render(request,'cars/booked.html',
    {'bi' : bookingId,
      'username' : username})