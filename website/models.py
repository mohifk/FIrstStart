
from django.db import models
class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    massage= models.TextField()
    created_date= models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
# Create your models here.
