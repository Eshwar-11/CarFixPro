from django.urls import path
from . import views

urlpatterns = [
    path("landing_page", views.index, name="landing_page"),
    path("thank-you", views.thank_you),
    path("customer_login", views.customer_login, name="customer_login"),
    path("manager_login", views.manager_login),
    path("technician_login", views.technician_login),
    path("technician_dashboard", views.technician_dashboard, name="technician_dashboard"),
    path("customer_dashboard", views.customer_dashboard, name="customer_dashboard"),
    path("manager_dashboard", views.manager_dashboard, name="manager_dashboard"),
    path("manager_pending_approvals", views.manager_pending_approvals, name="manager_pending_approvals"),
    path("technician_pending_appointments", views.technician_pending_appointments, name="technician_pending_appointments"),
    path("book_appointment", views.book_appointment, name="book_appointment"),
    path("add_vehicle", views.add_vehicle, name="add_vehicle"), 
    path("remove_vehicle", views.remove_vehicle, name="remove_vehicle"), 
    path("technician_registration", views.technician_registration, name="technician_registration"),
    path("add_technician_skills", views.add_technician_skills, name="add_technician_skills"),
    path("delete_technician_skills", views.delete_technician_skills, name="delete_technician_skills"),
    path("add_technician_skills/<str:test_number>", views.add_technician_skills_choices, name="add_technician_skills_choices"),
    path("delete_technician_skills/<str:test_number>", views.delete_technician_skills_choices, name="delete_technician_skills_choices"),
    path("manager_appointment_finish_approval", views.manager_appointment_finish_approval, name="manager_appointment_finish_approval"),
    path("logout_customer", views.logout_customer, name="logout_customer"), 
    path("logout_manager", views.logout_manager, name="logout_manager"), 
    path("logout_technician", views.logout_technician, name="logout_technician"),
    path("delete_technician", views.delete_technician, name="delete_technician"),
    path("pay_technician", views.pay_technician, name="pay_technician"),
    path("delete_appointment", views.delete_appointment, name="delete_appointment"),
    path("view_vehicle", views.view_vehicle, name="view_vehicle"),
    path("view_appointments", views.view_appointments, name="view_appointments"),
    path("view_technician_profile", views.view_technician_profile, name="view_technician_profile"),
    path("view_inprocess_appointments", views.view_inprocess_appointments, name="view_inprocess_appointments"),
    path("customer_thank_you", views.customer_thank_you, name="customer_thank_you"),
    path("customer_dashboard_thank_you", views.customer_dashboard_thank_you, name="customer_dashboard_thank_you")
]