from django.db import models
from ..accounts.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='category')
    category=models.CharField(max_length=250)
    slug=models.SlugField(max_length=100, unique=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.category)
        super().save(*args, **kwargs)
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
    stock=models.PositiveIntegerField(default=0)
    isbn=models.CharField(max_length=13, unique=True)
    language=models.CharField(max_length=50, default='Uzbek')
    pages=models.PositiveIntegerField()
    published_date=models.DateField()
    cover_image=models.ImageField(upload_to='images/')
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    author=models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    slug=models.CharField(max_length=200, blank=True, null=True, unique=True )

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)           
    discount = models.DecimalField(max_digits=5, decimal_places=2) 
    valid_from = models.DateTimeField(default=timezone.now)
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=True)
    
    def str(self):
        return self.code

    def is_valid(self):
        now = timezone.now()
        return self.active and self.valid_from <= now <= self.valid_to
    

class WishList(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='wishlist')
    book=models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True, related_name='wishlist')
    slug=models.CharField(max_length=200, blank=True, unique=True)

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.book.title) 
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return f"{self.book}"