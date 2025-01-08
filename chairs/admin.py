from django.contrib import admin
from chairs.models import chairset

class chairadmin(admin.ModelAdmin):
    list_display=('chairs_des','chairs_title','chairs_img','chairs_price')

admin.site.register(chairset,chairadmin)    

# Register your models here.
