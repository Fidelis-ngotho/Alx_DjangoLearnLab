from django.contrib import admin
from .models import Book, Library

# Register the models to appear in the admin interface
admin.site.register(Book)
admin.site.register(Library)


# Register your models here.
