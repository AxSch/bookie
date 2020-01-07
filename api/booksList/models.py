from django.db import models
from django.conf import settings
from books.models import Book

# Create your models here.

User = settings.AUTH_USER_MODEL


class WishList(models.Model):
    name = models.CharField(max_length=32)
    books = models.ManyToManyField(Book, blank=True, related_name='books')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
