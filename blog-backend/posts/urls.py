from django.urls import path
from .views import PostListCreateAPIView, PostRetrieveAPIView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveAPIView.as_view(), name='post-detail'),
]