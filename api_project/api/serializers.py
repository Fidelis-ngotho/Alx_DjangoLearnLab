from rest_framework import serializers
from .models import Book  # Ensure you have a Book model defined

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields from the Book model
