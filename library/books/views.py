from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm


def home(request):

    books = Book.objects.filter(rating__gt=6)

    return render(request, 'home.html', context={'books': books})


def detail_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'detail.html', context={'book': book})


def create_book(request):
    if request.method == 'POST':
        bookform = BookForm(request.POST)
        if bookform.is_valid():
            bookform.save()
            return redirect('home')
    return render(request, 'create.html', context={'form': BookForm()})


def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        bookform = BookForm(request.POST, instance=book)
        if bookform.is_valid():
            bookform.save()
            return redirect('home')
    return render(request, 'update.html',context={'form': BookForm(instance=book)})


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('home')