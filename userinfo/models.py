from django.db import models

# Create your models here.
class contactEnquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    psw=models.CharField(max_length=50)
    pswrepeat=models.CharField(max_length=50)