from .models import Category, Author, Book
from ..accounts.serializers import UserSerializer
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Category
        fields=['id', 'user', 'category', 'slug']


class AuthorSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Author
        fields=['id','user', 'full_name', 'bio', 'birth_date', 'photo']

class BookSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    category=CategorySerializer(read_only=True)
    author=AuthorSerializer(read_only=True)
    class Meta:
        model=Book
        fields=['title', 'user', 'description', 'price', 'discount_price', 'stock', 'isbn', 'language', 'pages', 'published_date', 
                'cover_image', 'category', 'author']
