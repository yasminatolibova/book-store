from django.db import models
from ..accounts.models import User
# Create your models here.


class Category(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='category')
    category=models.CharField(max_length=250)
    slug=models.SlugField(max_length=100, unique=True)
    def __str__(self):
        return self.category

class Author(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='author')
    full_name=models.CharField(max_length=250)
    bio=models.TextField()
    birth_date=models.DateField()
    photo=models.ImageField(upload_to='authors/', blank=True, null=True)

    def __str__(self):
        return self.full_name
    

class Book(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='book')
    title=models.CharField(max_length=250)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    discount_price=models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    stock=models.BooleanField(default=True)
    isbn=models.CharField(max_length=13, unique=True)
    language=models.CharField(max_length=50, default='Uzbek')
    pages=models.PositiveIntegerField()
    published_date=models.DateField()
    cover_image=models.ImageField(upload_to='images/')
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    author=models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
    

