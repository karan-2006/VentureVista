from django.urls import path
from . import views

app_name = "destinations"

urlpatterns = [
    path('', views.index, name='destinations'),
    path('<int:id>/', views.destination_detail, name='destination_detail'),
    path('book-destination/<int:id>/', views.confirm_destination_booking, name='confirm_destination_booking'),
]
