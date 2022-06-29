from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Post, Rate
from .serializers import PostsSerializer, RateSerializer


class CustomNumberPagination(PageNumberPagination):
    """Custom pagination"""
    page_size = 10


class PostsListAPIView(ListAPIView):
    """An API view to show list of posts"""
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    pagination_class = CustomNumberPagination


class RateCreateAPIView(CreateAPIView):
    """An API view to create a rate"""
    serializer_class = RateSerializer
    queryset = Rate.objects.all()
