from .models import Cart, Cartitem, Order, Orderitem
from ..accounts.serializers import  UserSerializer
from rest_framework import serializers


class CartSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Cart
        fields=['user', 'created_at', 'updated_at', 'is_active', 'get_total_items', 'get_total_price' ]
        
    

class CartitemSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Cartitem
        fields=['user', 'cart', 'book', 'quantity', 'add_at']
        read_only_fields=['book', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Order
        fields=['user', 'status', 'total_amount', 'created_at', 'updated_at', 'address', 'phone', 'payment_method', ]
        

class OrderitemSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Orderitem
        fields='__all__'
   