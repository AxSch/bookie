from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# anthropology - study of humans
# can consist of psychology
# sociology
# philosophy
# Biology
# so books can fall into three categories:
#  Social
#  Cultural
#  Biological

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    summary = models.TextField(max_length=128)
    author = models.CharField(max_length=64)
    date_added = models.DateTimeField(auto_now_add=True)
    cover_art = models.ImageField(upload_to='book_covers/', blank=True)
    SOCIAL = 'SO'
    CULTURAL = 'CU'
    BIOLOGICAL = 'BI'
    CATEGORY_CHOICES = [
        (SOCIAL, 'Social'),
        (CULTURAL, 'Cultural'),
        (BIOLOGICAL, 'Biological')
    ]
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=SOCIAL)
    rating = models.DecimalField(default=0.0, max_digits=2, decimal_places=1, blank=True, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    amazon_link = models.CharField(max_length=512)
    have_read = models.BooleanField(default=False, blank=True)
