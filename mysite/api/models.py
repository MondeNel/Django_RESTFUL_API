from django.db import models

class BlogPost(models.Model):
    """
    Represents a single blog post entry in the system.
    
    Attributes:
        title (str): The title of the blog post (max length 200 characters).
        content (str): The main body content of the blog post.
        created_at (datetime): Timestamp of when the blog post was created.
        updated_at (datetime): Timestamp of when the blog post was last updated.
    
    Methods:
        __str__: Returns the title of the blog post.
    """
    # The title of the blog post (max length 200 characters)
    title = models.CharField(max_length=200)
    
    # The main content of the blog post
    content = models.TextField()

    # Automatically set the timestamp when the blog post is created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Automatically update the timestamp when the blog post is modified
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns the title of the blog post when called.
        """
        return self.title
