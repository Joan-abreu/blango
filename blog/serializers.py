from rest_framework import serializers
from .models import Post, Comment, Tag, AuthorProfile

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'value']

class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'created_at', 'modified_at', 'published_at', 'title', 'slug', 'summary', 'content', 'tags']

class CommentSerializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'creator', 'post', 'content', 'created_at']

class AuthorProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = AuthorProfile
        fields = ['id', 'user', 'bio']
