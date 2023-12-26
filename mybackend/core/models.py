from django.db import models

# Create your models here.

#Post Model content has string, tags are an array of 
#3*(no. of images) that give image tags (No array field in sqlite)
class Post(models.Model):
    content = models.TextField(blank=False)
    timePosted = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=512,blank=True, null=True)

    def __str__(self):
        return f"Post {self.id}: {self.content}"
    
#Image model has the image field(Location in media folder), 
#each image is connected to a post
class Image(models.Model):
    image = models.ImageField(upload_to = 'store/img', null=True, blank=True, default='Users/abhishekvenkata/Desktop/abhishek.jpg')
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Image {self.id}"