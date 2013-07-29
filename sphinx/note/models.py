#-*- coding:utf-8-*-
from django.db import models

class Notepad(models.Model):
    """notepad data storm"""
    basicstr = models.CharField(max_length=20, verbose_name=u"短地址")
    sharestr = models.CharField(max_length=20, verbose_name=u"分享地址")
    text = models.TextField()
<<<<<<< HEAD
    
    pub_time = models.DateTimeField(auto_now=True, auto_now_add=True)
    mod_time = models.DateTimeField(auto_now=True, auto_now_add=True)
    
=======
    pub_time = models.DateTimeField(auto_now=True, auto_now_add=True)
    mod_time = models.DateTimeField(auto_now=True, auto_now_add=True)

>>>>>>> f04b899b9ef74c6317ef4d8e778cc52120f68dbf
    def __unicode__(self):
        return self.basicstr
