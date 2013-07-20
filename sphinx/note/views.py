#-*- coding:utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts  import render_to_response
from django.template import loader, Context

from note.models import Notepad

from note.forms import NotepadForm

import string 
import random 
import hashlib


def generateStr():
    """
        Generate the random string  
    """
    seed_str    = string.lowercase
    seed_digits = string.digits 
    aStr = ''
    tNum = ''
    lenStr = random.randint(6,10)
    aStr   += ''.join( random.choice(seed_str) for i in xrange(lenStr) )
    tNum   += ''.join( random.choice(seed_digits) for i in xrange(2) )
    return aStr+tNum
      
def index(request):
    """  Define the index request.      
        当没有输入内容的时候，随即生成的字符串url保存到数据库里面
    """
    t = loader.get_template('index.html')
    c = Context()
    
    baStr = generateStr()
    shStr = generateStr()
    #实现数据库里面保存把生成的字符串保存 
    t1 = Notepad(basicStr = baStr, shareStr = shStr, text = "")
    t1.save()
    #print t1    
    return HttpResponseRedirect('/%s'%baStr) 

def noteprocess(request, basic):
    """
        process function.    
    """
    if request.method == "POST":
        noteform = NotepadForm(request.POST)
        if noteform.is_valid:
            mytext = noteform.clean_data['text']   
            t1 = Notepad(basicStr = baStr, shareStr = shStr, text = mytext)
            t1.save()
    t = loader.get_template('noteprocess.html')
    c = Context()
    mynotepad = Notepad.objects.get(basicStr = basic)
    c['mynotepad'] = mynotepad 
    return HttpResponse( t.render(c) )

