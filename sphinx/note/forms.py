#-*- coding:utf-8 -*-
from note.models import Notepad
from django import forms

class notepadform(forms.Form):
    text=forms.CharField(label="Text", widget=forms.Textarea(attrs={'style':'width:100%;height:30em'}))

