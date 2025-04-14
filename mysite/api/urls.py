from django.urls import path
from . import views

# URL configuration for BlogPost API endpoints
urlpatterns = [
    # Endpoint for listing all blog posts or creating a new one
    # GET  → List all blog posts
    # POST → Create a new blog post
    path(
        'blogposts/',
        views.BlogPostListCreate.as_view(),
        name='blogpost-list-create'
    ),

    # Endpoint for retrieving, updating, or deleting a specific blog post by ID
    # GET    → Retrieve a blog post by its primary key (pk)
    # PUT    → Update an existing blog post
    # PATCH  → Partially update an existing blog post
    # DELETE → Delete a blog post
    path(
        'blogposts/<int:pk>/',
        views.BlogPostRetrieveUpdateDestroy.as_view(),
        name='blogpost-detail'
    ),
]
