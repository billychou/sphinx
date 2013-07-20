#-*- coding:utf-8 -*-
from django.shortcuts  import redirect, render

from note.models import Notepad
from note.forms import NotepadForm
from note.func import generateStr


def index(request):
    """  Define the index request.      
        当没有输入内容的时候，随即生成的字符串url保存到数据库里面
    """
    baStr = generateStr()
    shStr = generateStr()
    #实现数据库里面保存把生成的字符串保存 
    t1 = Notepad(basicStr = baStr, shareStr = shStr, text = "")
    t1.save()
    return redirect('/%s' % baStr) 

def noteprocess(request, basic):
    """
        process function.    
    """
    if request.method == "POST":
        noteform = NotepadForm(request.POST)
        if noteform.is_valid():
            mytext = noteform.clean_data['text']   
            t1 = Notepad(basicStr = baStr, shareStr = shStr, text = mytext)
            t1.save()
    else:
        noteform = NotepadForm()    
    mynotepad = Notepad.objects.get(basicStr = basic)
    return render(request, 'noteprocess.html',{'noteform':noteform,'mynotepad':mynotepad })

