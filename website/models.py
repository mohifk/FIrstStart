

from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject=models.CharField(max_length=255,null=True,blank=True)
    message= models.TextField()
    created_date= models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
# Create your models here.
    class Meta :
        ordering=['-created_date']
        #verbose_name= 'پست'
        #verbose_name_plural='پستها'
# Create your models here.
    def __str__(self):
        return self.name
class Newsletter(models.Model):
    email=models.EmailField()
    def __str__(self):
        return self.email