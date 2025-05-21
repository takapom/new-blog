from django.shortcuts import render


from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets

#投稿の一覧表示と新規作成
class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer

#個別の投稿の詳細表示
class PostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#CRUD処理
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer