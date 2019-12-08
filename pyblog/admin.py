# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from pyblog.models import Post,PostCategory,Comment



@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    pass
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass