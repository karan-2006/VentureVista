from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from .models import Offer, Slide, Profile
from .forms import CustomUserCreationForm, ProfileUpdateForm


def index(request):
    categories = ["Flights", "Hotels", "Holidays", "Trains", "Cabs", "Bus"]
    offers = Offer.objects.all()
    slides = Slide.objects.all()
    return render(request, "core/index.html", {
        "offers": offers,
        "categories": categories,
        "slides": slides
    })


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def update_profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'accounts/update_profile.html', {'form': form})


@login_required
def confirm_offer_booking(request, offer_id):
    offer = get_object_or_404(Offer, id=offer_id)
    return render(request, 'core/confirm_offer_booking.html', {'offer': offer})


def offer_booking_success(request, offer_id):
    offer = get_object_or_404(Offer, id=offer_id)
    return render(request, 'core/offer_booking_success.html', {'offer': offer})
