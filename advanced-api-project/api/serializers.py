from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# BookSerializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation for publication_year
    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# AuthorSerializer with nested BookSerializer
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serialization of books

    class Meta:
        model = Author
        fields = ['name', 'books']

# The BookSerializer serializes all fields of the Book model and includes custom validation.
# The AuthorSerializer nests the BookSerializer to dynamically include related books.
