from django.urls import path
from .views import (
    booking_home, book_flight, confirm_flight_booking,
    book_hotel, confirm_hotel_booking,
    book_homestay, confirm_homestay_booking,
    book_package, confirm_package_booking,
    booking_success
)

app_name = "booking"

urlpatterns = [
    path("", booking_home, name="booking"),
    path("book-flight/", book_flight, name="book_flight"),
    path("confirm-flight/<int:flight_id>/", confirm_flight_booking, name="confirm_flight_booking"),
    
    path("book-hotel/", book_hotel, name="book_hotel"),
    path("confirm-hotel/<int:hotel_id>/", confirm_hotel_booking, name="confirm_hotel_booking"),

    path("book-homestay/", book_homestay, name="book_homestay"),
    path("confirm-homestay/<int:homestay_id>/", confirm_homestay_booking, name="confirm_homestay_booking"),

    path("book-package/", book_package, name="book_package"),
    path("confirm-package/<int:package_id>/", confirm_package_booking, name="confirm_package_booking"),

    path("booking-success/", booking_success, name="booking_success"),
]
