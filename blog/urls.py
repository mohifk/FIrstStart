from operator import index
from django.urls import path
from blog.views import *

app_name='blog'

urlpatterns = [

    path ('',blog_view,name='index'),
    path ('single',blog_single,name='single'),
    path ('<str:name>/<str:family>/<int:age>',test,name='test'),

]