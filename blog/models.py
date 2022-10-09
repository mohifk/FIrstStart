
from email.policy import default
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
class category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name
class post(models.Model):
    image=models.ImageField(upload_to='media/blog/',default='blog/defult.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=255)
    content= models.TextField()
    #tage=
    category=models.ManyToManyField(category)
    count_views= models.IntegerField(default=0)
    status= models.BooleanField(default=False)
    publish_date= models.DateTimeField(null=True)
    create_date= models.DateTimeField(auto_now_add=True)
    update_date= models.DateTimeField(auto_now=True)

    class Meta :
        ordering=['create_date']
        #verbose_name= 'پست'
        #verbose_name_plural='پستها'
# Create your models here.
    def __str__(self):
        return "{} :::: ID is : {}".format(self.title,self.id)