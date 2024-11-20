from django.urls import path
from views import list_books

urlpatterns = [
    # URL pattern for the function-based view
    path('books/', views.list_books, name='list_books'),

    # URL pattern for the class-based view, expecting a library ID
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
