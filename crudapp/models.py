
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Author Name")
    email = models.EmailField(max_length=277, verbose_name="Author Email",null=True)

    def __str__(self):
        return str(self.id)

class Book(models.Model):
    book_name = models.CharField(max_length=100, verbose_name="Book Name")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Author")
    published_date = models.DateField(verbose_name="Published Date")
    edition = models.CharField(max_length=50, verbose_name="Edition")

    def __str__(self):
        return str(self.id)
