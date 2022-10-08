from multiprocessing import context
from django.shortcuts import render
from blog.models import post
def blog_view(request):
    return render(request,'blog/blog-home.html')
def blog_single(request):
    context={'name':'mohi','lastname':'fk'}
    return render(request,'blog/blog-single.html',context)
def test(request):
    posts=post.objects.all()
    #post=post.objects.filter(status=0)
    context={'posts':posts} ## the means is evry where {%posts%} means post.objects.all()
    return render(request,'test.html',context)
# Create your views here.
