from django.contrib import admin
from .models import CustomerInfo, Vehicle, Location, Service, Appointment, AppointmentStatus, ManagerInfo, TechnicianInfo, TechnicianSkills
# Register your models here.
admin.site.register(CustomerInfo)
admin.site.register(Vehicle)
admin.site.register(Location)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(AppointmentStatus)
admin.site.register(ManagerInfo)
admin.site.register(TechnicianInfo)
admin.site.register(TechnicianSkills)