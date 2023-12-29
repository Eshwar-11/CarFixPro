from django.db import models
from django.utils import timezone
from passlib.hash import pbkdf2_sha256
from django.core import validators
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
import re

# Create your models here.
class CustomerInfo(models.Model):

    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    address = models.TextField()
    phone = models.CharField(max_length=10)
    email_id = models.EmailField(primary_key=True, null=False)
    c_number = models.CharField(max_length=16)
    passwd = models.CharField(max_length=256, null=True)

    def verify_password(self, p):
        return pbkdf2_sha256.verify(p, self.passwd)
    
    def __str__(self):
        return f"{self.fname} {self.lname}"

class Vehicle(models.Model):

    def validate_capital_or_digit(value):
        if not any(char.isupper() or char.isdigit() for char in value):
            raise ValidationError(
                'The value must contain at least one capital letter or digit.',
                code='invalid_capital_or_digit',)
        
    CHOICES  = (('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Hatchback', 'Hatchback'), ('Crossover', 'Crossover'))

    customer_email = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE)
    vin = models.CharField(max_length=17, primary_key=True, validators=[validate_capital_or_digit, MinLengthValidator(17), MaxLengthValidator(17)])
    model = models.CharField(max_length=50)
    year = models.CharField(max_length=4, validators=[MinLengthValidator(4), MaxLengthValidator(4)])
    color = models.CharField(max_length=10)
    mfg_company = models.CharField(max_length=20)
    vtype = models.CharField(max_length=10, choices=CHOICES, null=False)

    def __str__(self):
        return f"{self.vin} {self.mfg_company} {self.model}"

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    pincode = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.address} {self.state} {self.pincode}"

class Service(models.Model):

    CHOICES_SERVICES  = (('Maintenance and Repairs', 'Maintenance and Repairs'), 
                        ('Diagnostic Services', 'Diagnostic Services'), 
                        ('Body and Paint Services', 'Body and Paint Services'), 
                        ('Detailing Services', 'Detailing Services'), 
                        ('Customization Services', 'Customization Services'), 
                        ('Towing and Recovery Services', 'Towing and Recovery Services'), 
                        ('Pre-Purchase Inspection', 'Pre-Purchase Inspection'),
                        ('Rental and Leasing Services', 'Rental and Leasing Services'),
                        ('Consultation and Advice', 'Consultation and Advice'))
    
    CHOICES_VTYPE  = (('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Hatchback', 'Hatchback'), ('Crossover', 'Crossover'))
    
    service_type = models.CharField(max_length=30, choices=CHOICES_SERVICES)
    vehicle_type = models.CharField(max_length=30, choices=CHOICES_VTYPE)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['service_type', 'vehicle_type'], name='composite_pk')
        ]

    def __str__(self):
        return f"{self.vehicle_type} {self.service_type} - ${self.price}"


class Appointment(models.Model):

    appointment_id = models.AutoField(primary_key=True)
    date = models.DateField()
    vehicle_id = models.CharField(max_length=17)
    vehicletype = models.CharField(max_length=30)  
    customer_email = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    service_details = models.CharField(max_length=250)
    total_price = models.DecimalField(decimal_places=2, max_digits=8)
    manager_start_approval = models.BooleanField(default=False)
    manager_finish_approval = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.appointment_id} {self.customer_email} {self.date}"

class ManagerInfo(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    address = models.TextField()
    phone = models.CharField(max_length=10)
    email_id = models.EmailField(primary_key=True, null=False)
    acc_number = models.CharField(max_length=16)
    salary = models.IntegerField()
    SSN = models.CharField(max_length=9, validators=[MinLengthValidator(9), MaxLengthValidator(9)])

    passwd = models.CharField(max_length=256, null=True)

    def verify_password(self, p):
        return pbkdf2_sha256.verify(p, self.passwd)
    
    def __str__(self):
        return f"{self.fname} {self.lname}"

class TechnicianInfo(models.Model):
    SSN = models.CharField(max_length=9, validators=[MinLengthValidator(9), MaxLengthValidator(9)])
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    address = models.TextField()
    phone = models.CharField(max_length=10)
    email_id = models.EmailField(primary_key=True, null=False)
    acc_number = models.CharField(max_length=16)
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    salary_last_credit = models.DateField()
    mngr = models.ForeignKey(ManagerInfo, on_delete=models.CASCADE)
    hire_date = models.DateField()
    location = models.CharField(max_length=100)
    passwd = models.CharField(max_length=256, null=True)

    def save_salary_last_credit(self):
        today = timezone.now().date()
        self.salary_last_credit = today
        self.save()

    def verify_password(self, p):
        return pbkdf2_sha256.verify(p, self.passwd)
    
    def __str__(self):
        return f"{self.fname} {self.lname}"
    
class TechnicianSkills(models.Model):
    email_id = models.ForeignKey(TechnicianInfo, on_delete=models.CASCADE, null=False)
    service_type = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.email_id} {self.service_type}"

class AppointmentStatus(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    service_detail = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    completed_by_technician = models.ForeignKey(TechnicianInfo, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.appointment.appointment_id} {self.service_detail}"

@receiver(post_save, sender=Appointment)
def create_appointment_status(sender, instance, created, **kwargs):
    if created:
        service_details_list = instance.service_details.split(', ')

        for service_detail in service_details_list:
            AppointmentStatus.objects.create(appointment=instance, service_detail=service_detail.strip())