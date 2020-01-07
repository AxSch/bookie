from rest_framework import serializers
from .models import WishList
from books.serializers import BookWishListSerializer


class WishListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    books = BookWishListSerializer(many=True)

    class Meta:
        model = WishList
        fields = ["id", "name", "books", "owner", "is_public"]
