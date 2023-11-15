from django.shortcuts import render

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