from django.contrib import admin
from .models import Book, Author, Library, Librarian, UserProfile

# Register the models to appear in the admin interface
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(UserProfile)
