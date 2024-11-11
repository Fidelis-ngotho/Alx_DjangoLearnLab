# Delete Operation

In this operation, we will delete the book with the title "Nineteen Eighty-Four" from the database.

## Code:
```python
from bookshelf.models import Book

# Retrieve the book you want to delete
retrieved_book = Book.objects.get(title="Nineteen Eighty-Four")

# Print the book details before deletion
print(retrieved_book)

# Delete the book
retrieved_book.delete()

# Attempt to retrieve the book again (this should fail, as the book has been deleted)
try:
    retrieved_book = Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:
    print("The book has been deleted.")
