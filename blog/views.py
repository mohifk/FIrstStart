from itertools import count
from django import views
from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger

def blog_view(request,**kwargs):
    posts=Post.objects.filter(publish_date__lte=timezone.now(),status=1) 
    if kwargs.get('cat_name') !=None:
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') !=None:
        posts=posts.filter(author__username=kwargs['author_username'])
    posts= Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts=posts.get_page(page_number)
    except PageNotAnInteger :
        posts=posts.get_page(1)
    except EmptyPage:
        posts=posts.get_page(1)
    context={'posts':posts}                                  ## the means is evry where {%posts%} means posts
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    posts=Post.objects.filter(status=1) 
    post_=get_object_or_404(Post,pk=pid,status=True)
    post_.count_views+=1
    post_.save()
    p='Prev Post'
    n='Next Post'
    if pid>1 and pid < len(posts)+1:
        for i in range (1,len(posts)-1) :
            if posts[i] == post_ :
                next1=posts[i+1]
                prev1=posts[i-1]
            
    elif pid==len(posts)+1 :
        next1=posts[len(posts)-1] 
        next1.title=''
        n=''
        prev1=posts[len(posts)-2] 
    elif pid == 1:
        next1=posts[1]
        prev1=posts[0]
        prev1.title=''
        p=''                  
    context={'post':post_,'next1':next1,'prev1':prev1,'p':p,'n':n}
    return render(request,'blog/blog-single.html',context)

def test(request):
    return render(request,'test.html')

def blog_search(request):
    posts=Post.objects.filter(status=1)
    if request.method == 'GET' :
        if s:= request.GET.get('s'):
            posts=posts.filter(content__contains=s)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

