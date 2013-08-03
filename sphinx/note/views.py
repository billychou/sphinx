#-*- coding:utf-8 -*-
from django.shortcuts  import redirect
from django.shortcuts import render
from note.models import Notepad
from note.forms import NotepadForm
from note.utils import generatestr


def index(request):
    """  Define the index request.      
        当没有输入内容的时候，随即生成的字符串url保存到数据库里面
    """
    bastr = generatestr()
    shstr = generatestr()
    #实现数据库里面保存把生成的字符串保存 
    t1 = Notepad(basicstr=bastr, sharestr=shstr, text="")
    t1 = Notepad(basicstr=bastr, sharestr=shstr, text="")
    t1.save()
    return redirect('/%s' %bastr)

def noteprocess(request, basic):
    """
        process function.    
    """
    if request.method == "POST":
        mytext = request.POST.get('myform', '')
    else:
        mytext = request.GET.get('myform', '')
    mynotepad = Notepad.objects.get(basicstr=basic)
    mynotepad.text = mytext 
    mynotepad.save()
     
    return render(request, 'noteprocess.html', {'mynotepad':mynotepad})

def shareprocess(request, share):
    """
        share address
    """
    mytext = Notepad.objects.get(sharestr=share)
    current_url = request.path
    return render(request, 'shareprocess.html', {'mytext':mytext, 'current_url':current_url})
