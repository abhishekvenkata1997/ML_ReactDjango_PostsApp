from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post, Image
from .serializers import PostSerializer, ImageSerializer

#Image view set can do all CRUD apis with just queryset and serializer name
#no need to connect each url with a new view
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

#Post view can do all CRUD apis
#added two GET APIs search and imagesearch to allow search on content and search on tags operations
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        ordering = self.request.query_params.get('ordering','timePosted')
        return self.queryset.order_by(ordering)
    
    @action(detail=False,methods=['GET'])
    def search(self, request, *args, **kwargs):
        try:    
            search_term = request.query_params.get('search','')
            print(search_term)

            #get all posts from queryset and filter if search term contains content value
            queryset = self.get_queryset().filter(content__icontains=search_term)
            serializer = self.get_serializer(queryset,many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'detail':str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['GET'])
    def imagesearch(self, request, *args, **kwargs):
        try:
            search_term = request.query_params.get('search','')
            print(search_term)
            #get all posts from queryset and filter if search term contains values in tags array
            queryset = self.get_queryset().filter(tags__icontains=search_term)
            serializer = self.get_serializer(queryset,many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'detail':str(e)}, status=status.HTTP_400_BAD_REQUEST)


