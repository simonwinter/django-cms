"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from cms_django.models import TextBlock, ImageBlock


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class TextBlockTest(TestCase):

	def test_simple_textBlock_success(self):
		t = TextBlock()
		t.text = "Blah Blah"
		t.save()
		
		self.assertEqual(t.text, "Blah Blah")