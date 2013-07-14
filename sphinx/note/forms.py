#-*- coding:utf-8 -*-
from note.models import Notepad
from django import forms

class NotepadForm(forms.ModelForm):
    class Meta:
        model = Notepad
        fields = ('text',)
