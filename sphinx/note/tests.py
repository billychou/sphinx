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
    def setup(self):
        Notepad.objects.create(basicStr="hello", shareStr="world", text="helloworld")
        Notepad.objects.create(basicStr="linuxworld", shareStr="Abckdd12", text="welcome to my world. this is excellent. Very good!")
    
    def test_notepad_can_create_text(self):
        """
            test if the notepad text is created or not
        """
        myhello = Notepad.objects.get(basicStr="hello")
        mylinuxworld = Notepad.objects.get(basicStr="linuxworld")
        self.assertEqual(myhello.text, "helloworld")
        self.assertEqual(mylinuxworld.text, "welcome to my world. this is excellent. Very good!")


    def test_notepad_can_create_sharestr(self):
        """test if the notepad sharestr is created or not            
        """
        self.assertEqual(Notepad.objects.get(basicStr="hello").shareStr, "world")
        self.assertEqual(Notepad.objects.get(basicStr="linuxworld").shareStr, "Abckdd12")








