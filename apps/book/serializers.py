from .models import Category, Author, Book, Coupon
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

class CouponApplySerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50, required=True)

    def validate_code(self, value):
        try:
            coupon = Coupon.objects.get(code__iexact=value)  
        except Coupon.DoesNotExist:
            raise serializers.ValidationError("Bunday promo kod mavjud emas.")
        
        if not coupon.is_valid():
            raise serializers.ValidationError("Promo kod muddati tugagan yoki faol emas.")
        
        return coupon