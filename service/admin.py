from django.contrib import admin
from service.models import Service
class serviceAdmin(admin.ModelAdmin):
    list_display=('service_des','service_title','service_price','service_img','service_img1','service_img2','service_img3')

admin.site.register(Service,serviceAdmin)
# Register your models here.
