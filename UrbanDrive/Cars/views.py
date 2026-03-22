from django.shortcuts import render,redirect
from .models import Car,Booking,CarRating
from Users.models import Users
from django.utils import timezone
from datetime import datetime
from .decorators import session_login_required
from .utils import calculate_flexible_rent

def cars(request):
    return render(request,'cars/cars.html')

def car_detail(request,id):
    car = Car.objects.get(id=id)
    rating = CarRating.objects.filter(car=id)
    return render(request,'cars/car_detail.html',{'car' : car , 'rating' : rating})

@session_login_required
def booking_form(request, id):

    user_id = request.session.get('id')
    car = Car.objects.get(id=id)
    booked = None

    if user_id:
        user = Users.objects.get(id=user_id)
    else:
        return redirect("login")

    if request.method == "POST":
        aadhar = request.POST.get("aadhar")
        dob = request.POST.get("dob")
        licence = request.POST.get("licence")
        exp = request.POST.get("valid")
        phoneNum = request.POST.get("mn")

        current_time = timezone.now().strftime("%Y%m%d%H%M%S")
        booking_id = "BD" + aadhar.replace(" ", "")[8:] + phoneNum.replace(" ", "")[6:] + current_time

        
        start_dt = datetime.fromisoformat(request.session.get('start'))
        end_dt = datetime.fromisoformat(request.session.get('end'))

 
        total_rent = calculate_flexible_rent(
            start_dt,
            end_dt,
            daily_rate=car.rent,          
            hourly_rate=car.rent / 24     
        )

        booked = Booking.objects.create(
            id=booking_id,
            user=user,
            car=car,
            aadhar=aadhar,
            aadhar_dob=dob,
            licence=licence,
            licence_exp=exp,
            mobile_no=phoneNum,
            rent=total_rent,   
            start=start_dt,
            end=end_dt,
        )

        return redirect("confirm_booking", booking_id=booked.id)

    return render(request, 'cars/bookingform.html', {'booking': booked})

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


def review(request, id):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('cmt')

        user = request.user
        car = Car.objects.get(id=id)

        if not Booking.objects.filter(user=user, car=car).exists():
            return render(request, 'error.html', {
                'error': "You cannot rate this car because you never booked it"
            })

        if CarRating.objects.filter(user=user, car=car).exists():
            return render(request, 'error.html', {
                'error': "You already reviewed this car"
            })

        CarRating.objects.create(
            user=user,
            car=car,
            rating=rating,
            comment=comment,
        )

        return redirect('car_detail', car.id)

    return render(request, 'cars/add_review.html')