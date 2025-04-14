from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

# Create your views here.

class BlogPostListCreate(generics.ListCreateAPIView):
    """
    API view to retrieve and create blog posts.

    GET: Returns a list of all blog posts.
    POST: Creates a new blog post from the request data and returns the created post.
    """
    # Define the queryset that will be used to retrieve blog posts.
    queryset = BlogPost.objects.all()

    # Define the serializer class that will be used to convert data to and from JSON format.
    serializer_class = BlogPostSerializer
