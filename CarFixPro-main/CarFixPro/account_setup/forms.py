from django import forms
from .models import Appointment, AppointmentStatus, TechnicianInfo

class CustomerRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=30, label="First name", error_messages={
        "required" : "Please enter your first name!",
        "max_length" : "Your first name should not exceed 30 characters!"
    })
    last_name = forms.CharField(max_length=30, label="Last name")
    address = forms.CharField(max_length=100, label="Address")
    phone = forms.CharField(max_length=10, label="Phone number")
    email = forms.EmailField(label="Email ID")
    credit_card_number = forms.CharField(max_length=16, label="Credit card number")
    password = forms.CharField(max_length=32, required=True, widget=forms.PasswordInput)

class CustomerLoginForm(forms.Form):
    username = forms.EmailField(label="Your email is your username")
    password = forms.CharField(max_length=32, required=True, widget=forms.PasswordInput)

class AddVehicleForm(forms.Form):

    CHOICES  = [('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Hatchback', 'Hatchback'), ('Crossover', 'Crossover')]

    vin = forms.CharField(max_length=17, label="VIN")
    model = forms.CharField(max_length=50, label="Model")
    year = forms.CharField(max_length=4, label="Year")
    color = forms.CharField(max_length=10, label="Color")
    mfg_company = forms.CharField(max_length=20, label="Brand")
    vtype = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'form-control'}), label="Type")

class BookAppointment(forms.Form):

    CHOICES_SERVICES  = (('Maintenance and Repairs', 'Maintenance and Repairs'), 
                        ('Diagnostic Services', 'Diagnostic Services'), 
                        ('Body and Paint Services', 'Body and Paint Services'), 
                        ('Detailing Services', 'Detailing Services'), 
                        ('Customization Services', 'Customization Services'), 
                        ('Towing and Recovery Services', 'Towing and Recovery Services'), 
                        ('Pre-Purchase Inspection', 'Pre-Purchase Inspection'),
                        ('Rental and Leasing Services', 'Rental and Leasing Services'),
                        ('Consultation and Advice', 'Consultation and Advice'))

    vehicle_details = forms.ChoiceField(choices=(), widget=forms.Select, label="Select your vehicle")
    location_details = forms.ChoiceField(choices=(), widget=forms.Select, label="Select servicing location")
    date = forms.DateField(label="Date of appointment")
    services_details = forms.MultipleChoiceField(choices=CHOICES_SERVICES, widget=forms.CheckboxSelectMultiple, label="Select services")

    def __init__(self, *args, **kwargs):
        vehicle_choices = kwargs.pop('vehicle_choices', [])
        location_choices = kwargs.pop('location_choices', [])

        super(BookAppointment, self).__init__(*args, **kwargs)

        default_option = ('', 'Select...')
        vehicle_choices = [default_option] + vehicle_choices
        location_choices = [default_option] + location_choices

        self.fields['vehicle_details'].choices = vehicle_choices
        self.fields['location_details'].choices = location_choices

class ManagerLoginForm(forms.Form):
    username = forms.EmailField(label="Your email is your username")
    password = forms.CharField(max_length=32, required=True, widget=forms.PasswordInput)


class AppointmentApprovalForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['manager_start_approval']

class TechnicianRegistrationForm(forms.Form):
    ssn = forms.CharField(max_length=9, label="SSN")

    first_name = forms.CharField(max_length=30, label="First name", error_messages={
        "required" : "Please enter your first name!",
        "max_length" : "Your first name should not exceed 30 characters!"
    })
    last_name = forms.CharField(max_length=30, label="Last name")
    address = forms.CharField(max_length=100, label="Address")
    phone = forms.CharField(max_length=10, label="Phone number")
    email = forms.EmailField(label="Email ID")
    acc_number = forms.CharField(max_length=16, label="Bank account number")
    hire_date = forms.DateField(label="Hire date")
    location = forms.ChoiceField(choices=(), widget=forms.Select, label="Technician servicing location")
    password = forms.CharField(max_length=32, required=True, widget=forms.PasswordInput, label="Enter temporary password")

    def __init__(self, *args, **kwargs):
        location_choices = kwargs.pop('location_choices', [])

        super(TechnicianRegistrationForm, self).__init__(*args, **kwargs)

        default_option = ('', 'Select...')
        location_choices = [default_option] + location_choices
        self.fields['location'].choices = location_choices

class AddTechnicianSkillsForm(forms.Form):
    technician = forms.ChoiceField(choices=(), widget=forms.Select, label="Select technician")

    def __init__(self, *args, **kwargs):
        technician_choices = kwargs.pop('technician_choices', [])

        super(AddTechnicianSkillsForm, self).__init__(*args, **kwargs)

        default_option = ('', 'Select...')
        technician_choices = [default_option] + technician_choices

        self.fields['technician'].choices = technician_choices


class AddTechnicianSkillsChoicesForm(forms.Form):
    technician = forms.ChoiceField(choices=(), widget=forms.Select(attrs={'disabled':'disabled'}), label="Select technician", required=False)
    services = forms.MultipleChoiceField(choices=(), widget=forms.CheckboxSelectMultiple, label="Select services")

    def __init__(self, *args, **kwargs):
        technician_choices = kwargs.pop('technician_choices', [])
        services_choices = kwargs.pop('service_choices', [])

        super(AddTechnicianSkillsChoicesForm, self).__init__(*args, **kwargs)

        self.fields['technician'].choices = technician_choices
        self.fields['services'].choices = services_choices

class DeleteTechnicianSkillsForm(forms.Form):
    technician = forms.ChoiceField(choices=(), widget=forms.Select, label="Select technician")

    def __init__(self, *args, **kwargs):
        technician_choices = kwargs.pop('technician_choices', [])

        super(DeleteTechnicianSkillsForm, self).__init__(*args, **kwargs)

        default_option = ('', 'Select...')
        technician_choices = [default_option] + technician_choices

        self.fields['technician'].choices = technician_choices


class DeleteTechnicianSkillsChoicesForm(forms.Form):
    technician = forms.ChoiceField(choices=(), widget=forms.Select(attrs={'disabled':'disabled'}), label="Select technician", required=False)
    services = forms.MultipleChoiceField(choices=(), widget=forms.CheckboxSelectMultiple, label="Select services")

    def __init__(self, *args, **kwargs):
        technician_choices = kwargs.pop('technician_choices', [])
        services_choices = kwargs.pop('service_choices', [])

        super(DeleteTechnicianSkillsChoicesForm, self).__init__(*args, **kwargs)

        self.fields['technician'].choices = technician_choices
        self.fields['services'].choices = services_choices

class TechnicianLoginForm(forms.Form):
    username = forms.EmailField(label="Your email is your username")
    password = forms.CharField(max_length=32, required=True, widget=forms.PasswordInput)

class TechnicianCompletionForm(forms.ModelForm):
    class Meta:
        model = AppointmentStatus
        fields = ['completed']

class ManagerAppointmentFinishApprovalForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['manager_finish_approval']


class DeleteTechnicianForm(forms.Form):
    technician = forms.ChoiceField(choices=(), widget=forms.Select, label="Select technician")

    def __init__(self, *args, **kwargs):
        technician_choices = kwargs.pop('technician_choices', [])

        super(DeleteTechnicianForm, self).__init__(*args, **kwargs)

        default_option = ('', 'Select...')
        technician_choices = [default_option] + technician_choices

        self.fields['technician'].choices = technician_choices

class SalaryApprovalForm(forms.ModelForm):
    class Meta:
        model = TechnicianInfo
        fields = []

class RemoveVehicleForm(forms.Form):
    vehicle = forms.ChoiceField(choices=(), widget=forms.Select, label="Select vehicle")

    def __init__(self, *args, **kwargs):
        vehicle_choices = kwargs.pop('vehicle_choices', [])

        super(RemoveVehicleForm, self).__init__(*args, **kwargs)

        default_option = ('', 'Select...')
        vehicle_choices = [default_option] + vehicle_choices

        self.fields['vehicle'].choices = vehicle_choices

class DeleteAppointmentForm(forms.Form):
    appointment = forms.ChoiceField(choices=(), widget=forms.Select, label="Select appointment")

    def __init__(self, *args, **kwargs):
        appointment_choices = kwargs.pop('appointment_choices', [])

        super(DeleteAppointmentForm, self).__init__(*args, **kwargs)

        default_option = ('', 'Select...')
        appointment_choices = [default_option] + appointment_choices

        self.fields['appointment'].choices = appointment_choices