from django.db import models
from django.db import models

# Author model
class Author(models.Model):
    name = models.CharField(max_length=100)  # Author's name

    def __str__(self):
        return self.name

# Book model
class Book(models.Model):
    title = models.CharField(max_length=200)  # Book's title
    publication_year = models.PositiveIntegerField()  # Year of publication
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # Relationship to Author

    def __str__(self):
        return self.titles

# The Author model represents an author of books. Each author can have multiple books.
# The Book model represents individual books, linked to an author via a foreign key.

# Create your models here.
