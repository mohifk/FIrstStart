from multiprocessing import context
from django.shortcuts import render
def blog_view(request):
    return render(request,'blog/blog-home.html')
def blog_single(request):
    context={'name':'mohi','lastname':'fk'}
    return render(request,'blog/blog-single.html',context)
# Create your views here.
