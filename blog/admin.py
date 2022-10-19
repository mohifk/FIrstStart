from django.contrib import admin
from blog.models import Post,category
from django_summernote.admin import SummernoteModelAdmin
#@admin.register(post)       # -----this or down
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'create_date'
    empty_value_display= '-empty-'
    #fields=('title',)
    #exclude=('title',)
    list_display=('title','author','count_views','status','publish_date')
    list_filter=('status','author')
    ordering=['-create_date']
    search_fields=['title','content']
    summernote_fields=('content')
admin.site.register(category)
admin.site.register(Post,PostAdmin)     # ------ or this or up

