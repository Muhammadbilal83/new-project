from django.contrib import admin
from contact.models import contact

class contactadmin(admin.ModelAdmin):
    list_display=('contact_email','Contact_title','Contact_img')

admin.site.register(contact,contactadmin)    


# Register your models here.
