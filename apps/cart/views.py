from django.shortcuts import render

# Create your views here.
from .models import Cart, Cartitem, Order
from rest_framework import permissions,  generics, status
from rest_framework.response import Response
from .serializers import CartitemSerializer, CartSerializer, OrderSerializer, OrderitemSerializer, Orderitem
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes



class CartListCreateView(generics.ListCreateAPIView):
    serializer_class=CartSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class=CartSerializer
    permission_classes=[permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartitemListCreateView(generics.ListCreateAPIView):
    
    serializer_class=CartitemSerializer
    permission_classes=[permissions.IsAuthenticated]
    

    def get_queryset(self):
        return Cartitem.objects.filter(car__user=self.request.user)

    def perform_create(self, serializer):
        cart, _ =Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)

    
class CartitemDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class=CartitemSerializer
    permission_classes=[permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field='id'

    def get_queryset(self):
        return Cartitem.objects.filter(user=self.request.user)

   


class OrderListCreateView(generics.ListCreateAPIView):
    
    serializer_class=OrderSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    
class OrderDetailView(generics.RetrieveAPIView):
    
    serializer_class=OrderSerializer
    permission_classes=[permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field='id'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def checkout_cart(request, cart_id):
    cart=get_object_or_404(Cart, id=cart_id, user=request.user)

    if not cart.cartitem_set.exists():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    order=Order.objects.create(user=request.user)
    total_price=0

    for cart_item in cart.cartitem_set.all():
        Orderitem.objects.create(
            order=order,
            book=cart_item.book,
            quantity=cart_item.quantity,
            price=cart_item.book.price,
        )

        total_price+=cart_item.quantity*cart_item.book.price

    cart.cartitem_set.all().delete()
    serializer=OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

    