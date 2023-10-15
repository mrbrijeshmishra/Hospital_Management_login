from django.contrib import admin
from .models import *


class patientAdmin(admin.ModelAdmin):
    list_display = ("id","fname","lname","username","address1","state",
                    "city","pincode","pic")
    
class doctorAdmin(admin.ModelAdmin):
    list_display = ("id","fname","lname","username","address1","state",
                    "city","pincode","pic")

class contactUsAdmin(admin.ModelAdmin):
    list_display = ("id","name","email","message")

admin.site.register(patient,patientAdmin)
admin.site.register(doctor,doctorAdmin)
admin.site.register(contactUs,contactUsAdmin)