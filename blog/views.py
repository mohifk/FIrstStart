
from django.shortcuts import render,get_object_or_404
from blog.models import post
def blog_view(request):
    posts=post.objects.filter(status=1)
    context={'posts':posts} ## the means is evry where {%posts%} means post.objects.all()
    return render(request,'blog/blog-home.html',context)
def blog_single(request):
    context={'name':'mohi','lastname':'fk'}
    return render(request,'blog/blog-single.html',context)

def test(request,pid):
    #Post=post.objects.get(id=pid)
    Post=get_object_or_404(post,pk=pid)
    context={'post':Post}
    return render(request,'test.html',context)
# Create your views here.
