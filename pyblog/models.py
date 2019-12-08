# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class PostCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey('PostCategory',null=True, blank=True,on_delete=models.DO_NOTHING)
    published = models.BooleanField(default=False)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    
    STATUS_VISIBLE = 'VISIBLE'
    STATUS_HIDDEN = 'HIDDEN'
    STATUS_MODERATED = 'MODERATED'
    
    STATUS_CHOICES = (
        (STATUS_VISIBLE,'VISIBLE')
        (STATUS_HIDDEN,'HIDDEN')
        (STATUS_MODERATED,'MODERATED')
    )
    
    post = models.ForeignKey('Post',on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    status = models.CharField(max_length=20,default=STATUS_VISIBLE,choices=STATUS_CHOICES)
    moderation_text = models.CharField(max_length=200,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{} - {} (status={})'.format(self.author_name,self.text[:20],self.status)