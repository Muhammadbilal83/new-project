from django.contrib import admin
from bedset.models import bedset

class bedadmin(admin.ModelAdmin):
    list_display=('bed_des','bed_title','bed_img','bed_price')

admin.site.register(bedset,bedadmin)    

# Register your models here.
