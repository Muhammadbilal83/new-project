from django.db import models

class detail(models.Model):
    detail_titlt=models.CharField(max_length=200)
    detail_price=models.CharField(max_length=200)
    detail_img=models.FileField(upload_to='media/pic',null=True,default=None)

# Create your models here.
