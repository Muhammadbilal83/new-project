from django.db import models
from autoslug import AutoSlugField
class Service(models.Model):
    service_des=models.CharField(max_length=500)
    service_title=models.CharField(max_length=50)
    service_img=models.FileField(upload_to='media/form',max_length=250,null=True,default=None)
    service_price=models.TextField()
    service_img1=models.FileField(upload_to='media/form',max_length=250,null=True,default=None)
    service_img2=models.FileField(upload_to='media/form',max_length=250,null=True,default=None)
    service_img3=models.FileField(upload_to='media/form',max_length=250,null=True,default=None)
# Create your models here.
