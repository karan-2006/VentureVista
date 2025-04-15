from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("confirm-offer-booking/<int:offer_id>/", views.confirm_offer_booking, name="confirm_offer_booking"),
    path('offer-booking-success/<int:offer_id>/', views.offer_booking_success, name='offer_booking_success'),
    path("profile/", views.profile, name="profile"),
    path("profile/update/", views.update_profile, name="update_profile"),
]
