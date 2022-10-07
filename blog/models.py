
from django.db import models


class post(models.Model):
    #image=
    #author=
    title=models.CharField(max_length=255)
    content= models.TextField()
    #tage=
    #category=
    count_views= models.IntegerField(default=0)
    status= models.BooleanField(default=False)
    publish_date= models.DateTimeField(null=True)
    create_date= models.DateTimeField(auto_now_add=True)
    update_date= models.DateTimeField(auto_now=True)
# Create your models here.
