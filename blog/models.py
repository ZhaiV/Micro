from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=30,primary_key=True)
    nickname = models.CharField(max_length=30,default='userxxx')
    passwd = models.CharField(max_length=16)
    label = models.CharField(max_length=40)
    job = models.CharField(max_length=13)
    address = models.CharField(max_length=40)
    birthday = models.DateField(default="1992-12-12")
    def __unicode__(self):
        return self.email+self.passwd
