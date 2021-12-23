from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
class RegistrationTestCase(APITestCase):
    
    def test_register(self):
        data = {
            'username':'testcase',
            'email':'testcase@gmail.com',
            'password': 'Password123',
            'password2': 'Password123'
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_200_CREATED)