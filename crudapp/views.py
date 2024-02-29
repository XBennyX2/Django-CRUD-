
from django.shortcuts import render
from .models import Book, Author
from django.contrib import messages
from django.db.models import Q

def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    search_query = ""

    if request.method == "POST":
        if "create_book" in request.POST:
            book_name = request.POST.get("book_name")
            author_id = request.POST.get("author")
            author = Author.objects.get(id=author_id)
            published_date = request.POST.get("published_date")
            edition = request.POST.get("edition")
            Book.objects.create(
                book_name=book_name,
                author=author,
                published_date=published_date,
                edition=edition
            )
            messages.success(request, "Book added successfully")

        elif "update_book" in request.POST:
            book_id = request.POST.get("id")
            book_name = request.POST.get("book_name")
            author_id = request.POST.get("author")
            author = Author.objects.get(id=author_id)
            published_date = request.POST.get("published_date")
            edition = request.POST.get("edition")
            book = Book.objects.get(id=book_id)
            book.book_name = book_name
            book.author = author
            book.published_date = published_date
            book.edition = edition
            book.save()
            messages.success(request, "Book updated successfully")

        elif "delete_book" in request.POST:
            book_id = request.POST.get("id")
            Book.objects.get(id=book_id).delete()
            messages.success(request, "Book deleted successfully")

        elif "create_author" in request.POST:
            author_name = request.POST.get("author_name")
            author_email = request.POST.get("author_email")
            Author.objects.create(
                name=author_name,
                email=author_email
            )
            messages.success(request, "Author added successfully")

        elif "update_author" in request.POST:
            author_id = request.POST.get("id")
            author_name = request.POST.get("author_name")
            author_email = request.POST.get("author_email")
            author = Author.objects.get(id=author_id)
            author.name = author_name
            author.email = author_email
            author.save()
            messages.success(request, "Author updated successfully")

        elif "delete_author" in request.POST:
            author_id = request.POST.get("id")
            Author.objects.get(id=author_id).delete()
            messages.success(request, "Author deleted successfully")

        elif "search" in request.POST:
            search_query = request.POST.get("query")
            books = Book.objects.filter(
                Q(book_name__icontains=search_query) | 
                Q(author__name__icontains=search_query) | 
                Q(published_date__icontains=search_query) | 
                Q(edition__icontains=search_query)
            )
            authors = Author.objects.filter(
                Q(name__icontains=search_query) | 
                Q(email__icontains=search_query)
            )

    context = {"books": books, "authors": authors, "search_query": search_query}
    return render(request, "index.html", context=context)
