from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Patient, Doctor, Appointment, Prescription

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["name", "dob", "gender", "email", "phone", "address", "emergency_contact"]

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ["name", "department", "email", "phone", "room_no", "is_active"]

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["patient", "doctor", "date", "time", "reason", "status"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
        }

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ["notes", "medications"]