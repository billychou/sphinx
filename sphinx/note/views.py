#-*- coding:utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts  import render_to_response
from django.template import loader, Context

from note.models import Notepad


def index(req):
    """
        Define the index request 
    """
    t = loader.get_template('index.html')
    c = Context()
    
    return HttpResponse( t.render(c) )

def noteprocess(req, basic ):
    t = loader.get_template('noteprocess.html')
    c = Context()
    mynotepad = Notepad.objects.get(basicStr = basic)
    c['mynotepad'] = mynotepad 
    return HttpResponse( t.render(c) )

