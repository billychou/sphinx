from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts  import render_to_response

def index(req):
    return HttpResponse('<h1>Hello World</h1>')