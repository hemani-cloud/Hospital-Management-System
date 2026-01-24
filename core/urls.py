from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('booking/', views.booking, name='booking'),
    path("doctors/", views.doctors, name="doctors"),
    path('contact/', views.contact, name='contact'),
    path("appointment/<int:id>/", views.appointment_detail, name="appointment_detail"),
    path("payment/<int:id>/", views.payment, name="payment"),
    path("payment-success/<int:id>/", views.payment_success, name="payment_success"),
]

