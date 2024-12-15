from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls


urlpatterns = [
    # Add path for the feed
    path('feed/', views.FeedView.as_view(), name='feed'),  # Includes "feed/"
]

