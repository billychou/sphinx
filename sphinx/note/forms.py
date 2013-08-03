#-*- coding:utf-8 -*-
from note.models import Notepad
from django import forms

class NotepadForm(forms.Form):
    text = forms.CharField(label="Text")
