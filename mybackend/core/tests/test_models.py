from django.test import TestCase
from core.models import Post,Image

class PostModelTest(TestCase):

    def test_post_creation(self):
        #Test Post creation
        post = Post.objects.create(content="Test Content",tags="tags1, tags2, tags3")
        self.assertEqual(post.content, "Test Content")
        self.assertEqual(post.tags, "tags1, tags2, tags3")

    def test_post_str_rep(self):
        #Test Post String representation
        post = Post.objects.create(content="Test Content",tags="tags1, tags2, tags3")
        self.assertEqual(str(post), f"Post {post.id}: {post.content}")

class ImageModelTest(TestCase):

    def test_image_creation(self):
        # Test creating an image instance
        post = Post.objects.create(content="Test Content", tags="tags1, tags2, tags3")
        image = Image.objects.create(post=post, image="./../../media/store/img/miata.jpeg")
        self.assertEqual(image.post, post)
        self.assertEqual(image.image, "./../../media/store/img/miata.jpeg")

    def test_image_str_rep(self):
        #Test image string representation
        post = Post.objects.create(content="Test Content", tags="tags1, tags2, tags3")
        image = Image.objects.create(post=post, image="./../../media/store/img/miata.jpeg")
        self.assertEqual(str(image), f"Image {image.id}")
