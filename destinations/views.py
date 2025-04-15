from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Destination

def index(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations/index.html', {'destinations': destinations})

def destination_detail(request, id):
    destination = get_object_or_404(Destination, id=id)
    return render(request, 'destinations/detail.html', {'destination': destination})

@login_required
def confirm_destination_booking(request, id):
    destination = get_object_or_404(Destination, pk=id)
    return render(request, 'destinations/confirm_destination_booking.html', {'destination': destination})
