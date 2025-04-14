from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.response import Response
from rest_framework import status

# API view for listing and creating blog posts
class BlogPostListCreate(generics.ListCreateAPIView):
    """
    API view to retrieve and create blog posts.

    GET: Returns a list of all blog posts.
    POST: Creates a new blog post from the request data and returns the created post.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        """
        Custom DELETE method to delete a blog post and return a custom response.
        """
        BlogPost.objects.all().delete()
        return Response(
            {"message": "All blog posts have been deleted."},
            status=status.HTTP_204_NO_CONTENT
        )

# API view for retrieving, updating, or deleting a blog post by its primary key
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific blog post.

    GET: Returns the details of a specific blog post.
    PUT/PATCH: Updates the details of a specific blog post.
    DELETE: Deletes a specific blog post.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'  # Look up posts by primary key (ID)
