from django import template
from blog.models import Post, category
register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    posts =Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='posts')
def function():
    posts=Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value,arg=15):
    return value[:arg] + '...'

@register.inclusion_tag('blog/blog-popular.html')
def lastestposts(arg=4):
    posts=Post.objects.filter(status=1).order_by('-publish_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-category.html')
def postcategories():
    posts=Post.objects.filter(status=1)
    categories = category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}