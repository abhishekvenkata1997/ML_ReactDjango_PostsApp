from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class PostViewSet(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_search_action(self):
        response = self.client.get('/api/Post/search/',{'search':'search_term'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_image_action(self):
        response  = self.client.get('/api/Post/imagesearch/',{'search':'search_term'})
        self.assertEqual(response.status_code,status.HTTP_200_OK)