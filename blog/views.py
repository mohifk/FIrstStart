
from itertools import count
from django import views
from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from blog.models import post
from django.core.paginator import Paginator
def blog_view(request):
    
    #posts=post.objects.filter(status=1)
    posts=post.objects.filter(publish_date__lte=timezone.now())
   
    context={'posts':posts} ## the means is evry where {%posts%} means post.objects.all()
    return render(request,'blog/blog-home.html',context)
def blog_single(request):
    context={'name':'mohi','lastname':'fk'}
    return render(request,'blog/blog-single.html',context)

def test(request,pid):
    #Post=post.objects.get(id=pid)
    Post=get_object_or_404(post,pk=pid)
    Post.count_views=Post.count_views+1
    #Post.objects.filters(pk=pid).update(count_views=F('count_views')+1)
    Post.save()
    
   # p = Paginator(post, 2)
    #Post.objects.filter(pk=post.pk).update(views=F('views') + 1)
    
    context={'post':Post}
  
    
    
    return render(request,'test.html',context)
    
# Create your views here.
