from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import FlightBooking, HotelBooking, HomestayBooking, PackageBooking
from datetime import datetime

# -------------------------
# Booking Homepage
# -------------------------

def booking_home(request):
    tabs = [
        ("Flights", "flights"),
        ("Hotels", "hotels"),
        ("Homestays", "homestays"),
        ("Holiday Packages", "packages")
    ]

    context = {
        "flights": FlightBooking.objects.all(),
        "hotels": HotelBooking.objects.all(),
        "homestays": HomestayBooking.objects.all(),
        "packages": PackageBooking.objects.all(),
        "tabs": tabs,
    }
    return render(request, "booking/index.html", context)


# -------------------------
# Flight Booking
# -------------------------

def book_flight(request):
    departure = request.GET.get("departure", "")
    destination = request.GET.get("destination", "")
    departure_date = request.GET.get("departureDate", "")

    try:
        departure_date = datetime.strptime(departure_date, "%Y-%m-%d").date()
    except ValueError:
        return render(request, "booking/flight_results.html", {"error": "Invalid date format"})

    flights = FlightBooking.objects.filter(
        departure=departure,
        destination=destination,
        departure_date=departure_date
    )

    if not flights.exists():
        return render(request, "booking/flight_results.html", {"error": "No flights available"})

    return render(request, "booking/flight_results.html", {"flights": flights})

@login_required
def confirm_flight_booking(request, flight_id):
    flight = get_object_or_404(FlightBooking, id=flight_id)
    return redirect(f"{reverse('booking:booking_success')}?type=flight")

# -------------------------
# Hotel Booking
# -------------------------

def book_hotel(request):
    location = request.GET.get('hotelLocation')
    start_date = request.GET.get('hotelStartDate')
    end_date = request.GET.get('hotelEndDate')

    hotels = HotelBooking.objects.filter(
        location=location,
        check_in__lte=start_date,
        check_out__gte=end_date
    )

    if not hotels.exists():
        return render(request, "booking/hotel_results.html", {"error": "No hotels available"})

    return render(request, "booking/hotel_results.html", {"hotels": hotels})

@login_required
def confirm_hotel_booking(request, hotel_id):
    hotel = get_object_or_404(HotelBooking, id=hotel_id)
    return redirect(f"{reverse('booking:booking_success')}?type=hotel")

# -------------------------
# Homestay Booking
# -------------------------

def book_homestay(request):
    location = request.GET.get('homestayLocation')
    guests = request.GET.get('guests')

    homestays = HomestayBooking.objects.filter(location=location, guests=guests)

    if not homestays.exists():
        return render(request, "booking/homestay_results.html", {"error": "No homestays available"})

    return render(request, "booking/homestay_results.html", {"homestays": homestays})

@login_required
def confirm_homestay_booking(request, homestay_id):
    homestay = get_object_or_404(HomestayBooking, id=homestay_id)
    return redirect(f"{reverse('booking:booking_success')}?type=homestay")

# -------------------------
# Package Booking
# -------------------------

def book_package(request):
    destination = request.GET.get('packageDestination')
    start_date = request.GET.get('packageStartDate')
    end_date = request.GET.get('packageEndDate')

    packages = PackageBooking.objects.filter(
        destination=destination,
        start_date=start_date,
        end_date=end_date
    )

    if not packages.exists():
        return render(request, "booking/package_results.html", {"error": "No packages available"})

    return render(request, "booking/package_results.html", {"packages": packages})

@login_required
def confirm_package_booking(request, package_id):
    package = get_object_or_404(PackageBooking, id=package_id)
    return redirect(f"{reverse('booking:booking_success')}?type=package")

# -------------------------
# Booking Success Page
# -------------------------

def booking_success(request):
    booking_type = request.GET.get("type", "booking")
    return render(request, "booking/success.html", {"booking_type": booking_type})

