from django.contrib.auth.models import User
from django.http import response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from .models import Category, Note
class CategoryTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='example', password='Password@123')
        self.token = Token.objects.get(user__username='example')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.category = Category.objects.create(name='New Sports', website='https://newsports.com')
    
    def test_category_create(self):
        data = {
            'name': 'Sports',
            'website': 'https://sports.com'
        }
        response = self.client.post(reverse('category-create'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_category_list(self):
        response = self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_category_details(self):
        response = self.client.get(reverse('category-detail', args=(self.category.id, )))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_category_update(self):
        response = self.client.put(reverse('category-detail', args=(self.category.id, )))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_category_delete(self):
        response = self.client.delete(reverse('category-detail', args=(self.category.id, )))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        

class NoteTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='example', password='NewPassword123')
        self.token = Token.objects.get(user__username='example')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.category = Category.objects.create(name='New Sports', website='https://newsports.com')
        self.note = Note.objects.create(title='New Note', owner=self.user, 
                                        category=self.category, text='Wonderful Boy')
    
    def test_note_create(self):
        data = {
            'title': 'Create',
            'owner': self.user.id,
            'category': self.category.id,
            'text': 'Rich always create opportunities.'
        }
        response = self.client.post(reverse('note-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_note_list(self):
        response = self.client.get(reverse('note-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_note_detail(self):
        response = self.client.get(reverse('note-detail', args=(self.note.id, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_note_update(self):
        data = {
            'title':'Create - Updated',
            'owner': self.user.id,
            'category': self.category.id,
            'text': 'This one is coming with a better update'
        }
        response = self.client.put(reverse('note-detail', args=(self.note.id, )), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_note_delete(self):
        response = self.client.delete(reverse('note-detail', args=(self.note.id, )))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)