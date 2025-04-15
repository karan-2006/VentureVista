from django.contrib import admin
from .models import HomestayBooking, HotelBooking, PackageBooking, FlightBooking

@admin.register(FlightBooking)
class FlightBookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'airline_name', 'departure', 'destination', 'departure_date')
    search_fields = ('airline_name', 'departure', 'destination')

@admin.register(HomestayBooking)
class HomestayBookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'guests')
    search_fields = ('name', 'location')

@admin.register(HotelBooking)
class HotelBookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'check_in', 'check_out')
    search_fields = ('name', 'location')

@admin.register(PackageBooking)
class PackageBookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'destination', 'start_date', 'end_date')
    search_fields = ('name', 'destination')
