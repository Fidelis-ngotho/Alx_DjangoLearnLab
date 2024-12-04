from django.urls import path
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from django.urls import path, include

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')  # Registering the ViewSet

urlpatterns = [
    path('', include(router.urls)),  # This includes all routes registered with the router
]

from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
