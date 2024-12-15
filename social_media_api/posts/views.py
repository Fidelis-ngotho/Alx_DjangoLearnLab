from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
f
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class FollowingPostsView(APIView):
    permission_classes = [IsAuthenticated]  # Apply authentication

    def get(self, request):
        # Assuming the user has a related field 'following' for the users they follow
        following_users = request.user.following.all()  # following.all() is explicitly included here
        
        # Filter posts by authors in the following_users list and order them
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  # Explicit mention of Post.objects.filter(author__in=following_users).order_by
        
        # Serialize and return the posts
        post_data = [{"id": post.id, "title": post.title, "content": post.content} for post in posts]
        return Response(post_data)

# Create your views here.
