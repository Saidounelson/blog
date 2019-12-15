# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from pyblog.models import Post,PostCategory,Comment



@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'text',
        'published',
        'created_at',
    )
    list_filter = ('category__name',
                   'published')
    
    autocomplete_fields=['category']
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass