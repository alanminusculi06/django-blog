from django.contrib import admin
from myblog.core.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_date', 'published_date']
    search_fields = ['title', 'slug']
    ordering = ['-created_date']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
