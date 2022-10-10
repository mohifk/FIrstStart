
from itertools import count
from os import stat
from django import views
from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from blog.models import post

def blog_view(request):
    
    #posts=post.objects.filter(status=1)
    posts=post.objects.filter(publish_date__lte=timezone.now(),status=1) 
    context={'posts':posts} ## the means is evry where {%posts%} means post.objects.all()
    return render(request,'blog/blog-home.html',context)


def blog_single(request,pid):
    post_=get_object_or_404(post,pk=pid,status=1)
    post_.count_views+=1
    post_.save()
    context={'post':post_}
    return render(request,'blog/blog-single.html',context)
