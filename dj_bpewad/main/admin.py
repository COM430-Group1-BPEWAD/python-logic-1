from django.contrib import admin

from .models import patient, bpReadings
# Register your models here.

admin.site.register(patient)
admin.site.register(bpReadings)