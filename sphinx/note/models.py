#-*- coding:utf-8-*-
from django.db import models

class Notepad(models.Model):
    """notepad data storm"""
    #title       = models.CharField(max_length = 30, verbose_name = u"标题")
    basicStr =  models.CharField(max_length = 20, verbose_name = u"短地址")
    shareStr =  models.CharField(max_length = 20, verbose_name = u"分享地址")
    text     =  models.TextField()

    def __unicode__(self):
        return self.basicStr 
