from itertools import count
from django import views
from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from blog.models import post

def blog_view(request):
    
    posts=post.objects.filter(publish_date__lte=timezone.now(),status=1) 
    context={'posts':posts} ## the means is evry where {%posts%} means post.objects.all()
    return render(request,'blog/blog-home.html',context)


def blog_single(request,pid):
    post_=get_object_or_404(post,pk=pid,status=1)
    post_.count_views+=1
    post_.save()
    next1=post.objects.get(pk=pid)
    next1.id+=1
    prev1=post.objects.get(pk=pid)
    prev1.id-=1
    context={'post':post_,'next1':next1,'prev1':prev1}
    return render(request,'blog/blog-single.html',context)

