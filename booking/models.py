from django.db import models

class FlightBooking(models.Model):
    airline_name = models.CharField(max_length=100, default="Flight")
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_date = models.DateField()

    def __str__(self):
        return f"{self.airline_name}: {self.departure} → {self.destination} ({self.departure_date})"


class HotelBooking(models.Model):
    name = models.CharField(max_length=100, default="Hotel")
    location = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.name} in {self.location}"


class HomestayBooking(models.Model):
    name = models.CharField(max_length=100, default="Home")
    location = models.CharField(max_length=100)
    guests = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.location} ({self.guests} guests)"


class PackageBooking(models.Model):
    name = models.CharField(max_length=100, default="Holiday")
    destination = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.destination}"
