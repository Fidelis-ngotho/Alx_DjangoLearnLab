from django.contrib import admin
from django.contrib import admin
from .models import Book

# Register the Book model with customized admin interface
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in the list view
    list_filter = ('author', 'publication_year')  # Filters for admin sidebar
    search_fields = ('title', 'author')  # Fields to be searchable in admin

# Register your models here.
