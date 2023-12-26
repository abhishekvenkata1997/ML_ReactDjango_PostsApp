from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from core.models import Post, Image
from core.serializers import PostSerializer, ImageSerializer
import tensorflow as tf 
import io
import re

class PostSerializerTest(TestCase):
    
    def setUp(self):
        self.client = APIClient()

    def test_create_post_with_images(self):

        #assuming you have a sample image file for testing
        image_path = 'media/store/img/miata.jpeg'
        image_content = open(image_path, "rb").read()
        image_file = SimpleUploadedFile("test_image.jpg",image_content,content_type="image/jpeg")

        data = {
            "content" : "Your post content",
            "tags" : ["tag1","tag2"],
            "images" : [image_file  ]
        }

        response = self.client.post("/api/Post/", data, format="multipart")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Post.objects.count(),1)
        post = Post.objects.get()
        self.assertEqual(post.content,data["content"])
        self.assertEqual(re.search(r"'sports_car'", post.tags).group(0).strip("'"),'sports_car')
        self.assertEqual(post.images.count(),len(data['images']))


    def test_create_post_without_images(self):
        
        #Test creating a post with images
        data = {
            "content" : "Your post content",
            "tags" : ["tag1", "tag2"]
        }

        response = self.client.post("/api/Post/", data, format="json")

        self.assertEqual(response.status_code, 400)


    def test_create_post_with_invalid_image(self):

        #Test creating a post with an invalid format
        data = {
            "content" : "Your post content",
            "tags" : ["tag1","tag2"],
            "images" : ["invalid_image_data"]
        }

        response = self.client.post("/api/Post/", data, format="json")

        self.assertEqual(response.status_code, 400)
        self.assertEqual(Post.objects.count(),0)

    def test_create_post_with_empty_content(self):

        #Test creating a post with empty content
        data = {
            "content" : "",
            "tags" : ["tag1","tag2"],
        }
        response = self.client.post("/api/Post/",data,format="json")

        self.assertEqual(response.status_code,400)
        self.assertEqual(Post.objects.count(),0)