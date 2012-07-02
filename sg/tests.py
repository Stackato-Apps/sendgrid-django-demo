"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import TestCase
from django.test.client import Client


class EmailTest(TestCase):
    def test_returns_200(self):
        """
        Tests that email is sent when POSTing to sg/send
        """
        c = Client()
        response = c.post('/sg/send', {
          'username': 'foo',
          'password': 'bar',
          'from': 'from@from.com',
          'to': 'to@to.com',
          'subj': 'subj text',
          'body': 'body text',
          })

        self.assertEqual(200,response.status_code)

