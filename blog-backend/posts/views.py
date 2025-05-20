from django.shortcuts import render


from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer

class PostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer