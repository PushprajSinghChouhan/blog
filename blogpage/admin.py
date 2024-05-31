from django.contrib import admin
from blogpage.models import Post

class blogAdmin(admin.ModelAdmin):
    list_display=('title','content','created_at','image')

admin.site.register(Post, blogAdmin)
