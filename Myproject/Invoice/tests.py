# from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.

class TestListCreateInvoice(APITestCase):
    
    def test_creates_invoice(self):
        sample_index = {'title':"Hello", "desc":'Test'}
        response = self.client.post(reverse('index'), sample_index)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)