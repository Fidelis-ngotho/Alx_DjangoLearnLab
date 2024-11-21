from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Library Project!</h1>")

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Document

@permission_required('accounts.can_view', raise_exception=True)
def document_list(request):
    documents = Document.objects.all()
    return render(request, 'accounts/document_list.html', {'documents': documents})

@permission_required('accounts.can_create', raise_exception=True)
def document_create(request):
    if request.method == "POST":
        # Logic to create a document
        pass
    return render(request, 'accounts/document_create.html')

@permission_required('accounts.can_edit', raise_exception=True)
def document_edit(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == "POST":
        # Logic to edit the document
        pass
    return render(request, 'accounts/document_edit.html', {'document': document})

@permission_required('accounts.can_delete', raise_exception=True)
def document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    document.delete()
    return redirect('document_list')

# Create your views here.
