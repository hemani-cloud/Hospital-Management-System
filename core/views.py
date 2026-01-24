from django.shortcuts import render, redirect
from .models import Appointment
from .models import Doctor

def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'base.html')

def services(request):
    return render(request, 'base.html')

def booking(request):
    return render(request, 'base.html')

def contact(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment

def booking(request):
    if request.method == "POST":
        appointment = Appointment.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            mobile=request.POST.get("mobile"),
            service=request.POST.get("service"),
            appointment_date=request.POST.get("appointment_date"),
            appointment_time=request.POST.get("appointment_time"),
            message=request.POST.get("message"),
        )
        return redirect("appointment_detail", appointment.id)

    return render(request, "booking.html")


def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html")

# core/views.py
def appointment_detail(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    return render(request, "appointment_detail.html", {"appointment": appointment})

def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, "doctors.html", {"doctors": doctors})

def appointment_detail(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    return render(request, "appointment_detail.html", {"appointment": appointment})

def payment(request, id):
    appointment = get_object_or_404(Appointment, id=id)

    if request.method == "POST":
        # For now assume payment is successful
        return redirect("payment_success", id=appointment.id)

    return render(request, "payment.html", {"appointment": appointment})

def payment_success(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    return render(request, "payment_success.html", {"appointment": appointment})


