# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Books
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your tests here.
class LoginTestCase(TestCase):
    def setUp(self):
        user=User.objects.create_user(username='jeet', password='admin123')

    def test_user_login(self):
        login = self.client.login(username='jeet', password='admin123')
        response = self.client.get('/loginform/')
        self.assertTrue(login, "True")
        self.assertEqual(response.status_code, 302)

class BookTestCase(TestCase):
    def setUp(self):
        Books.objects.create(book_name='Python', author_name='Simranjeet') 

    def test_book_update_view(self):
        resp = self.client.get('/update/1/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "cmcas/update.html")
        self.assertHTMLEqual(
    '<p>Hello <b>world!</p>',
    '''<p>
        Hello  <b>world!
    </p>'''
)       
    
        

