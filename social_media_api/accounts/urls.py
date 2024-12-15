from django.urls import path
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
urlpatterns = [
    # Add paths for follow and unfollow
    path('follow/<int:user_id>/', views.FollowUserView.as_view(), name='follow-user'),  # Includes "follow/<int:user_id>"
    path('unfollow/<int:user_id>/', views.UnfollowUserView.as_view(), name='unfollow-user'),  # Includes "unfollow/<int:user_id>"
]

urlpatterns = [
    # Add path for the feed
    path('feed/', views.FeedView.as_view(), name='feed'),  # Includes "feed/"
]

