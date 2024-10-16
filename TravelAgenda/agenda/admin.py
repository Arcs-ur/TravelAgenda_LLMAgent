# admin.py
from django.contrib import admin
from .models import Agenda, Location, AgendaLocation

admin.site.register(Agenda)
admin.site.register(Location)
admin.site.register(AgendaLocation)
