from django.contrib import admin
from .models import Appointment   # keep only existing models
from .models import Doctor

admin.site.register(Appointment)


admin.site.register(Doctor)
