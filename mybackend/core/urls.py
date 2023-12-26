from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageViewSet, PostViewSet

#router connected a viewset, to allow rest all generic rest apis to work with them
router = DefaultRouter()
router.register('Image', ImageViewSet,basename='Image')
router.register('Post',PostViewSet, basename='Post')

#list of all urls accessible to user
print(router.urls)

urlpatterns = [
    path('api/', include(router.urls)),

    
]
