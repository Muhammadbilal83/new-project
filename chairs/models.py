from django.db import models

class chairset(models.Model):
    chairs_des=models.CharField(max_length=500)
    chairs_title=models.CharField(max_length=50)
    chairs_img=models.FileField(upload_to='media/pic',max_length=250,null=True,default=None)
    chairs_price=models.TextField()
    chairs_img1=models.FileField(upload_to='media/form',max_length=250,null=True,default=None)
    chairs_img2=models.FileField(upload_to='media/form',max_length=250,null=True,default=None)
    chairs_img3=models.FileField(upload_to='media/form',max_length=250,null=True,default=None)
# Create your models here.
