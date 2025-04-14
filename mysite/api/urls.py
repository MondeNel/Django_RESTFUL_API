from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for listing and creating blog posts
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blogpost-list-create'),

    # URL pattern for retrieving, updating, and deleting a specific blog post by its ID
    # pk = Primary Key, which is the ID of the blog post
    path('blogposts/<int:pk>/', views.BlogPostDetail.as_view(), name='blogpost-detail'),
]