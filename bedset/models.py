from django.db import models

class bedset(models.Model):
    bed_des=models.CharField(max_length=500)
    bed_title=models.CharField(max_length=50)
    bed_img=models.FileField(upload_to='media/pic',max_length=250,null=True,default=None)
    bed_price=models.TextField()
    bed_img1=models.FileField(upload_to='media/form',max_length=250,null=True,default=None)
    bed_img2=models.FileField(upload_to='media/form',max_length=250,null=True,default=None)
    bed_img3=models.FileField(upload_to='media/form',max_length=250,null=True,default=None)

# Create your models here.
