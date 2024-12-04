from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    def setUp(self):
        # Create sample books for testing
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2021)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2022)

        # API endpoints
        self.list_url = reverse('book-list')  # Assuming you used 'book-list' for ListAPIView
        self.detail_url = lambda pk: reverse('book-detail', args=[pk])  # For DetailAPIView

    def test_list_books(self):
        """Test retrieving a list of books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Ensure 2 books are returned

    def test_create_book(self):
        """Test creating a new book."""
        data = {"title": "Book Three", "author": "Author C", "publication_year": 2023}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)  # Ensure a new book is created

    def test_update_book(self):
        """Test updating an existing book."""
        data = {"title": "Updated Book One", "author": "Author A", "publication_year": 2021}
        response = self.client.put(self.detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book One")  # Verify the update

    def test_delete_book(self):
        """Test deleting a book."""
        response = self.client.delete(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)  # Ensure only one book remains

    def test_filter_books(self):
        """Test filtering books by author."""
        response = self.client.get(self.list_url, {"author": "Author A"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one book matches the filter

    def test_search_books(self):
        """Test searching books by title."""
        response = self.client.get(self.list_url, {"search": "Book One"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one book matches the search

    def test_order_books(self):
        """Test ordering books by publication_year."""
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Book One")  # Oldest book first

    def setUp(self):
    # Create a test user
    self.user = User.objects.create_user(username='testuser', password='testpassword')
    
    # Log in the user
    self.client.login(username='testuser', password='testpassword')

    # Create sample books
    self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2021)
    self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2022)
