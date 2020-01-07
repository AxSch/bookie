from django.db import models
from django.conf import settings
from books.models import Book

# Create your models here.

User = settings.AUTH_USER_MODEL


class BookList(models.Model):
    name = models.CharField(max_length=16)
    books = models.OneToOneField(Book, on_delete=models.CASCADE, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)