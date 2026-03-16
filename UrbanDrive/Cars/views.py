from django.shortcuts import render

def cars(request):
    return render(request,'cars/cars.html')

def car_detail(request,id):
    return render(request,'cars/car_detail.html')

def booking_form(request):
    return render(request,'cars/bookingform.html')

def confirm_booking(request):
    return render(request,'cars/confirm_booking.html')

def car_booked(request):
    return render(request,'cars/booked.html')