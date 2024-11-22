from django import forms
from .models import Book  # Assuming you have a Book model

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100, label='Book Title')
    author = forms.CharField(max_length=100, label='Author')

    # You can also add any additional validation here if needed
