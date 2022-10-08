from multiprocessing import context
from django.shortcuts import render
from blog.models import post
def blog_view(request):
    posts=post.objects.filter(status=1)
    context={'posts':posts} ## the means is evry where {%posts%} means post.objects.all()
    return render(request,'blog/blog-home.html',context)
def blog_single(request):
    context={'name':'mohi','lastname':'fk'}
    return render(request,'blog/blog-single.html',context)
def test(request,name,family,age):
    context={'name':name, 'family':family,'age':age}
    return render(request,'test.html',context)
# Create your views here.
