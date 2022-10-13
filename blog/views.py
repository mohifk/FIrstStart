from itertools import count
from django import views
from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from blog.models import Post

def blog_view(request):
    
    posts=Post.objects.filter(publish_date__lte=timezone.now(),status=1) 
    context={'posts':posts} ## the means is evry where {%posts%} means post.objects.all()
    return render(request,'blog/blog-home.html',context)


def blog_single(request,pid):
    post_=get_object_or_404(Post,pk=pid,status=1)
    post_.count_views+=1
    post_.save()
    try:
        next1=Post.objects.get(pk=pid+1)
    except:
        next1=Post.objects.get(pk=pid)
    try:
        prev1=Post.objects.get(pk=pid-1)
    except:
        prev1=Post.objects.get(pk=pid)
    context={'post':post_,'next1':next1,'prev1':prev1}
    return render(request,'blog/blog-single.html',context)

def test(request):
    return render(request,'test.html')

def blog_category(request,cat_name):
    posts=Post.objects.filter(status=1)
    posts=posts.filter(category__name=cat_name)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

