#-*- coding:utf-8 -*-
from django.shortcuts  import redirect, render

from note.models import notepad
from note.forms import notepadform
from note.func import generatestr


def index(request):
    """  Define the index request.      
        当没有输入内容的时候，随即生成的字符串url保存到数据库里面
    """
    bastr = generatestr()
    shstr = generatestr()
    #实现数据库里面保存把生成的字符串保存 
    t1 = notepad(basicStr=bastr, shareStr=shstr, text="")
    t1.save()
    return redirect('/%s' % bastr) 

def noteprocess(request, basic):
    """
        process function.    
    """
    if request.method == "POST":
        noteform = notepadform(request.POST)
        if noteform.is_valid():
            mytext = noteform.cleaned_data['text']   
            t1=notepad.objects.get(basicStr=basic)
            t1.text = mytext 
            t1.save()
    else:
        noteform = notepadform()
    mynotepad = notepad.objects.get(basicStr=basic)
    return render(request, 'noteprocess.html',{'noteform':noteform,'mynotepad':mynotepad })

