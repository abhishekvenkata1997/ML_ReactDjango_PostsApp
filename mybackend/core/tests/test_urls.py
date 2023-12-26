from django.test import TestCase
from django.urls import reverse
from rest_framework.routers import DefaultRouter
from core.views import ImageViewSet, PostViewSet

class UrlsTest(TestCase):
    
    def setUp(self):
        #Create a router and register viewsets
        self.router = DefaultRouter()
        self.router.register('Image',ImageViewSet, basename='Image')
        self.router.register('Post',PostViewSet,basename='Post')

    def test_image_url_resolves_to_view(self):

        #get the URL for the 'Image' view using reverse
        url = reverse('Image-list')

        #Use assert methods to check if the URL resolves to the correct view
        self.assertEqual(url, '/api/Image/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_url_resolves_to_view(self):

        #get url for the 'Post' view using reversee
        url = reverse('Post-list')

        #use assert methods to check if the URL resolves to the correct view
        self.assertEqual(url,'/api/Post/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
