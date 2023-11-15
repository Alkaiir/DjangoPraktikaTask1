from django.http import Http404
from django.shortcuts import render
from django.views import generic

from catalog.models import BookInstance, Author, Book, Genre


def index(request):
    # num_books_with_a = Book.objects.filter(title__icontains='a').count()
    # num_genres_with_a = Genre.objects.filter(name__icontains='a').count()
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        # 'num_books_with_a': num_books_with_a,
        # 'num_genres_with_a': num_genres_with_a
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, primary_key):
        try:
            book = Book.objects.get(pk=primary_key)
        except Book.DoesNotExist:
            raise Http404('Book does not exist')

        return render(request, 'catalog/book_detail.html', context={'book': book})