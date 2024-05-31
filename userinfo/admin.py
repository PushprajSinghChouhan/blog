from django.contrib import admin
from userinfo.models import contactEnquiry
# Register your models here.
class contactAdmin(admin.ModelAdmin):
    pass
admin.site.register(contactEnquiry,contactAdmin)