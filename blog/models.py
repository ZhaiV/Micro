from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=30,primary_key=True)
    nickname = models.CharField(max_length=30,default='userxxx')
    passwd = models.CharField(max_length=16)
    label = models.CharField(max_length=40)
    job = models.CharField(max_length=13)
    address = models.CharField(max_length=40)
    pothon = models.ImageField(upload_to = 'uploadl_img/', default = 'upload_img/defalt.jpg')
    birthday = models.DateField(default="1992-12-12")
    def __unicode__(self):
        return self.email+self.passwd
admin.site.register(User)
class Blog(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User)
    view_count = models.IntegerField()
    rank = models.IntegerField()
    create_at = models.DateField(auto_now_add= True)
    def __unicode__(self):
        return self.content
admin.site.register(Blog)        
class Comment(models.Model):
    pass

class Category(models.Model):
    name = models.CharField(max_length = 32, unique = true)
admin.site.register(Category)    
class Follows(models.Model):
    pass
admin.site.register(Follows)
class Fans(models.Model):
    pass 
admin.site.register(Fans)    
    
    
    
    
    