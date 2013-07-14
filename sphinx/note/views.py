#-*- coding:utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts  import render_to_response
from django.template import loader, Context

def index(req):
    """
        Define the index request 
    """
    return HttpResponse('<h1>Hello World</h1>')
