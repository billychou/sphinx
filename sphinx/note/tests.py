"""
    This file demonstrates writing tests using the unittest module. These will pass
    when you run "manage.py test".
    Replace this with more appropriate tests for your application.
"""
from django.test import TestCase
from note.models import Notepad
from django.test.client import Client

class NotepadTestCase(TestCase):
    """
        A simple test Notepad
    """
    def setUp(self):
        Notepad.objects.create(basicstr="hello", sharestr="world", text="helloworld")
        Notepad.objects.create(basicstr="linuxworld", sharestr="Abckdd12", text="welcome to my world. this is excellent. Very good!")
    
    def test_notepad_can_create_text(self):
        """
            test if the notepad text is created or not
        """
        myhello = Notepad.objects.get(basicstr="hello")
        mylinuxworld = Notepad.objects.get(basicstr="linuxworld")

        self.assertEqual(myhello.text, "helloworld")
        self.assertEqual(mylinuxworld.text, "welcome to my world. this is excellent. Very good!")


    def test_notepad_can_create_sharestr(self):
        """test if the notepad sharestr is created or not            
        """
        self.assertEqual(Notepad.objects.get(basicstr="hello").sharestr, "world")
        self.assertEqual(Notepad.objects.get(basicstr="linuxworld").sharestr, "Abckdd12")








