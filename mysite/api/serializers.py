from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    """
    Serializer for the BlogPost model.
    Converts BlogPost model instances to JSON format and vice versa.
    """
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']

    def create(self, validated_data):
        """
        Create and return a new BlogPost instance, given the validated data.
        """
        return BlogPost.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing BlogPost instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
