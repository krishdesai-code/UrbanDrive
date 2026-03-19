from django.urls import path
from . import views

urlpatterns = [
    path("",views.cars,name="car"),
    path("cars/<int:id>",views.car_detail,name="car_detail"),
    path("bookingForm/",views.booking_form,name="car_booking"),
    path("confirmBooking/",views.confirm_booking,name="confirm_booking"),
    path("carbooked/",views.car_booked,name="booked"),
]