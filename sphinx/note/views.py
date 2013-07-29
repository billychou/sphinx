#-*- coding:utf-8 -*-
from django.shortcuts  import redirect
from django.shortcuts import render
from note.models import Notepad
from note.forms import NotepadForm
<<<<<<< HEAD
from note.utils import generateStr
=======
from note.func import generatestr
>>>>>>> f04b899b9ef74c6317ef4d8e778cc52120f68dbf


def index(request):
    """  Define the index request.      
        当没有输入内容的时候，随即生成的字符串url保存到数据库里面
    """
    bastr = generatestr()
    shstr = generatestr()
    #实现数据库里面保存把生成的字符串保存 
<<<<<<< HEAD
    t1 = Notepad(basicstr=bastr, shareStr=shstr, text="")
=======
    t1 = Notepad(basicstr=bastr, sharestr=shstr, text="")
>>>>>>> f04b899b9ef74c6317ef4d8e778cc52120f68dbf
    t1.save()
    return redirect('/%s' %bastr)

def noteprocess(request, basic):
    """
        process function.    
    """
    if request.method == "POST":
        noteform = NotepadForm(request.POST)
        if noteform.is_valid():
            mytext = noteform.cleaned_data['text']   
            t1 = Notepad.objects.get(basicstr=basic)
            t1.text = mytext 
            t1.save()
            return redirect('/%s' % basic)
    else:
        noteform = NotepadForm()
    mynotepad = Notepad.objects.get(basicstr=basic)
    return render(request, 'noteprocess.html',{'noteform':noteform,'mynotepad':mynotepad})

