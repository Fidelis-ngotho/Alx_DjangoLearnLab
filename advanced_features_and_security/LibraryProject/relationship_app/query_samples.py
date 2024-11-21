from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author using filter
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        # Use filter to retrieve books with this specific author
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return None

# List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return None

# Retrieve the librarian for a library using Librarian.objects.get(library=...)
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        # Use Librarian.objects.get with the library as a filter
        return Librarian.objects.get(library=library)
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None
