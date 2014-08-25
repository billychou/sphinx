#-*- coding:utf-8-*-
from django.db import models

class Notepad(models.Model):
    """notepad data storm"""
    basicstr = models.CharField(max_length=20, verbose_name=u"短地址")
    sharestr = models.CharField(max_length=20, verbose_name=u"分享地址")
    text = models.TextField()
    pub_time = models.DateTimeField(auto_now=True, auto_now_add=True)
    mod_time = models.DateTimeField(auto_now=True, auto_now_add=True)
   
    def __unicode__(self):
        return self.basicstr
        
    @classmethod
    def create_a_object(cls, bastr, shstr):
        t1 = cls(basicstr=bastr, sharestr=shstr, text="")
        t1.save()
    
    @classmethod
    def get_object_by_basicstr(cls, bastr):
        return cls.objects.get(basicstr=bastr)

    @classmethod
    def get_object_by_sharestr(cls, shstr):
        return cls.objects.get(sharestr=shstr)

    @classmethod
    def get_all_objects(cls):
        return cls.objects.all()
