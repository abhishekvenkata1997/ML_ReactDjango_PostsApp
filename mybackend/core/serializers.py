import tensorflow as tf
import os
from keras.applications import MobileNetV3Large,MobileNetV3Small
from keras.applications.mobilenet_v3 import decode_predictions
from keras.preprocessing import image
from django.utils import timezone
from rest_framework import serializers
from .models import Image, Post

#model serializer to take JSON Data with id and image
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id','image']

#Post seriailzer that accepts many images, and updates on 4 fields
class PostSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'content', 'tags', 'images','timePosted']

    #create function to update the existing create function to help with tags and image addition
    def create(self, validated_data):
        images_data = self.context.get('request').data.getlist('images')
        post = Post.objects.create(**validated_data)

        #create a model from the imported models and add weights
        model = MobileNetV3Small(weights='imagenet')  # Load MobileNetV3Small
        tags = []

        #iterate through each image add image tags to list
        for image_data in images_data:
            
            created_image = Image.objects.create(post=post, image=image_data) #create image in db
            retrieved_image = Image.objects.get(pk=created_image.pk).image #get path of image
            
            # Base path
            base_path = '/Users/abhishekvenkata/Desktop/react_django/mybackend/media'

            # Append the filename to the base path using os.path.join
            img_path = os.path.join(base_path, retrieved_image.name) #get newly created image path
            img = tf.keras.preprocessing.image.load_img(img_path, target_size=(229, 229)) 
            img_array = tf.keras.preprocessing.image.img_to_array(img) 

            img_array = tf.expand_dims(img_array, axis=0)
            predictions = model.predict(img_array)

            # Decode predictions (using the custom function defined earlier)
            decoded_predictions = decode_predictions(predictions, top=3)[0]
            
            labels = [label for _, label, _ in decoded_predictions]
            tags.extend(labels)


        print("tags",tags)
        
        #add tags to post and return it
        post.tags = tags
        post.save()
        return post
