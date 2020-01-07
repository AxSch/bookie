from rest_framework import serializers
from .models import WishList
from books.serializers import BookSerializer


class WishListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    books = BookSerializer(many=True)

    class Meta:
        model = WishList
        fields = ["id", "name", "books", "owner", "is_public"]
