from django.contrib import admin
from detail.models import detail

class detailadmin(admin.ModelAdmin):
    list_display=('detail_titlt','detail_price','detail_img')

admin.site.register(detail,detailadmin)

# Register your models here.
