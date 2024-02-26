from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'author', 'date')
    list_filter = ('name', 'category', 'author', 'date')
    search_fields = ('name', 'text')
    raw_id_fields = ('author',)
    date_hierarchy = 'date'
    ordering = ['date']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)