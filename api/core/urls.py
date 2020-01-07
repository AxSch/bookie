from rest_framework.routers import DefaultRouter
from books.views import BooksViewSet
from booksList.views import WishListViewSet

router = DefaultRouter()
router.register(r'books', BooksViewSet, basename='books')
router.register(r'wishlist', WishListViewSet, basename='wishlist')

urlpatterns = router.urls
