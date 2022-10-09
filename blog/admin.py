from django.contrib import admin
from blog.models import post,category
#@admin.register(post)       # -----this or down
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    empty_value_display= '-empty-'
    #fields=('title',)
    #exclude=('title',)
    list_display=('title','author','count_views','status','publish_date')
    list_filter=('status','author')
    ordering=['-create_date']
    search_fields=['title','content']
admin.site.register(category)
admin.site.register(post,PostAdmin)     # ------ or this or up

