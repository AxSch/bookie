from rest_framework import serializers
from .models import WishList


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ['id', 'name', 'books', 'owner', 'is_public']
