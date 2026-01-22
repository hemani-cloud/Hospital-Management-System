from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    service = models.CharField(max_length=100, blank=True, null=True)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name or "Appointment"
        
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(help_text="Years of experience")
    image = models.ImageField(upload_to="doctors/")
    available_days = models.CharField(max_length=100)

    def __str__(self):
        return self.name