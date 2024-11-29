from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Library Project!</h1>")

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Document
@permission_required('accounts.can_view', raise_exception=True)
def book_list(request):
    books = book.objects.all()
    return render(request, 'accounts/book_list.html', {'books': books})

@permission_required('accounts.can_create', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        # Logic to create a book
        pass
    return render(request, 'accounts/book_create.html')

@permission_required('accounts.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(book, pk=pk)
    if request.method == "POST":
        # Logic to edit the book
        pass
    return render(request, 'accounts/book_edit.html', {'book': book})

@permission_required('accounts.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(book, pk=pk)
    book.delete()
    return redirect('book_list')

from django.shortcuts import render, redirect
from .forms import ExampleForm

def submit_book(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            
            # Optionally save the book to the database
            # Book.objects.create(title=title, author=author)
            
            return redirect('bookshelf:book_list')  # Redirect to the book list page after form submission
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})

# Create your views here.
