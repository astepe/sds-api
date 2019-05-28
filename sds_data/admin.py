from django.contrib import admin

from .models import SafetyDataSheet, Manufacturer

admin.site.register(SafetyDataSheet)
admin.site.register(Manufacturer)
