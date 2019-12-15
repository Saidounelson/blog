# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from pyblog.models import Post
# Create your views here.

def post_list(request):
    print("test")
    posts = Post.objects.all()
    print(posts)
    context = {
        'posts': posts,
    }
    
    return render(request,'pyblog/post_list.html', context)
    