# admin.py
from django.contrib import admin
from .models import Book, Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email"]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "book_name", "author", "published_date", "edition"]
