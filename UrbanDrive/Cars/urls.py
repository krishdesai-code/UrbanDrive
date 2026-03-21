from django.urls import path
from . import views

urlpatterns = [
    path("",views.cars,name="car"),
    path("<int:id>",views.car_detail,name="car_detail"),
    path("bookingForm/<int:id>/",views.booking_form,name="car_booking"),
    path("confirmBooking/<str:booking_id>/",views.confirm_booking,name="confirm_booking"),
    path("carbooked/",views.car_booked,name="booked"),
]