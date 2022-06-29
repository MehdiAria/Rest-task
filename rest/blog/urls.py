from django.urls import path

from .views import PostsListAPIView, RateCreateAPIView

urlpatterns = [
    path('api/posts', PostsListAPIView.as_view(), name='posts-list-api'),  # API endpoint for list of posts
    path('api/posts/rate', RateCreateAPIView.as_view(), name='rate-api'),  # API endpoint for creating rate
]
