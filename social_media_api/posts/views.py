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

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            # Create a notification
            Notification.objects.create(
                recipient=post.author,  # Assuming Post has an `author` field
                actor=request.user,
                verb="liked your post",
                target=post
            )
            return Response({"detail": "Post liked."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)


class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"detail": "Post unliked."}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

Step 3: Develop Notification System
3.1 View Notifications (in notifications/views.py)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = request.user.notifications.all()
        unread_notifications = notifications.filter(read=False)
        serialized_notifications = [
            {
                "id": notification.id,
                "actor": notification.actor.username,
                "verb": notification.verb,
                "timestamp": notification.timestamp,
                "read": notification.read
            } for notification in notifications
        ]
        return Response(serialized_notifications)

    def post(self, request):
        notifications = request.user.notifications.filter(read=False)
        notifications.update(read=True)
        return Response({"detail": "All notifications marked as read."})

Step 4: Define URL Patterns
4.1 Update posts/urls.py

from django.urls import path
from .views import LikePostView, UnlikePostView

urlpatterns = [
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]

4.2 Create notifications/urls.py

from django.urls import path
from .views import NotificationListView

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications'),
]

4.3 Include Notifications in Main URLs

In social_media_api/urls.py:

from django.urls import path, include

urlpatterns = [
    path('posts/', include('posts.urls')),
    path('notifications/', include('notifications.urls')),
]

Step 5: Test Features
Test Scenarios:

    Like and unlike posts using Postman or automated tests.
    Verify notifications are created when:
        A user likes a post.
        A user follows another user (extend functionality if needed).
        Comments are added to a post.
    Fetch unread notifications via /notifications/.

Example Tests:

# Like a post
POST /posts/1/like/
Authorization: Token <user-token>

# Fetch notifications
GET /notifications/
Authorization: Token <user-token>

Step 6: Documentation

Document the API endpoints, functionality, and test cases in a Markdown file (e.g., API_DOCUMENTATION.md) in your repository.

Let me know how you’d like to proceed with this implementation!


# Create your views here.
