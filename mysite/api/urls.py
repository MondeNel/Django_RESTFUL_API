from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for listing and creating blog posts
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blogpost-list-create'),
]