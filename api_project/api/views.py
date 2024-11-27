from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Queryset to retrieve all books
    serializer_class = BookSerializer  # Use the BookSerializer for serialization

# Create your views here.
