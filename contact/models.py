from django.db import models

class contact(models.Model):
    contact_email=models.EmailField(max_length=20)
    Contact_title=models.CharField(max_length=20)
    Contact_img=models.FileField(upload_to='media/form',max_length=250,null=True,default=None)

# Create your models here.
