from django import template
from blog.models import Post, category
register = template.Library()

@register.inclusion_tag('website_temp/blog_lastpost.html')
def lastestposts(arg=4):
    posts=Post.objects.filter(status=1).order_by('-publish_date')[:arg]
    return {'posts':posts}
