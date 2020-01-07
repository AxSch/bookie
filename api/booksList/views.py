from rest_framework import mixins
from .models import WishList
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import WishListSerializer

# Create your views here.


class WishListViewSet(
    GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
