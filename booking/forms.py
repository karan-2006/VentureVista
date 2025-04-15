from django import forms

class FlightBookingForm(forms.Form):
    departure = forms.CharField(
        label="From", 
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-transparent text-theme location-field', 
            'id': 'departure',
            'placeholder': 'Enter departure city',
            'required': True
        })
    )
    destination = forms.CharField(
        label="To", 
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-transparent text-theme location-field', 
            'id': 'destination',
            'placeholder': 'Enter destination city',
            'required': True
        })
    )
    departureDate = forms.DateField(
        label="Departure Date",
        widget=forms.DateInput(attrs={
            'class': 'form-control bg-transparent text-theme date-input',
            'id': 'departureDate',
            'type': 'date',
            'required': True
        })
    )

class HotelBookingForm(forms.Form):
    hotelLocation = forms.CharField(
        label="Destination",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-transparent text-theme location-field',
            'id': 'hotelLocation',
            'placeholder': 'Enter destination',
            'required': True
        })
    )
    hotelStartDate = forms.DateField(
        label="Check-in",
        widget=forms.DateInput(attrs={
            'class': 'form-control bg-transparent text-theme date-input',
            'id': 'hotelStartDate',
            'type': 'date',
            'required': True
        })
    )
    hotelEndDate = forms.DateField(
        label="Check-out",
        widget=forms.DateInput(attrs={
            'class': 'form-control bg-transparent text-theme date-input',
            'id': 'hotelEndDate',
            'type': 'date',
            'required': True
        })
    )

class HomestayBookingForm(forms.Form):
    homestayLocation = forms.CharField(
        label="Destination",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-transparent text-theme location-field',
            'id': 'homestayLocation',
            'placeholder': 'Enter destination',
            'required': True
        })
    )
    guests = forms.IntegerField(
        label="Guests",
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control bg-transparent text-theme',
            'id': 'guests',
            'placeholder': 'Enter number of guests',
            'required': True
        })
    )

class PackageBookingForm(forms.Form):
    packageDestination = forms.CharField(
        label="Destination",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-transparent text-theme location-field',
            'id': 'packageDestination',
            'placeholder': 'Enter destination',
            'required': True
        })
    )
    packageStartDate = forms.DateField(
        label="Start Date",
        widget=forms.DateInput(attrs={
            'class': 'form-control bg-transparent text-theme date-input',
            'id': 'packageStartDate',
            'type': 'date',
            'required': True
        })
    )
    packageEndDate = forms.DateField(
        label="End Date",
        widget=forms.DateInput(attrs={
            'class': 'form-control bg-transparent text-theme date-input',
            'id': 'packageEndDate',
            'type': 'date',
            'required': True
        })
    )
