from django.shortcuts import render

# Create your views here.
from .models import Category, Author, Book, WishList
from rest_framework import permissions,  generics, status
from rest_framework.response import Response
from .serializers import CategorySerializer, AuthorSerializer, BookSerializer, CouponApplySerializer, WishListSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .pagination import StandardResultsPagination



class CategoryListCreateView(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    pagination_class=StandardResultsPagination
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[permissions.IsAuthenticated, IsOwnerOrReadOnly]

    
class BookListCreateView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    filter_backends=[SearchFilter, OrderingFilter]
    search_fields=['title', 'author', 'category', 'isbn']
    ordering_fields=['language', 'stock']

    pagination_class = StandardResultsPagination
    
    
    def get_queryset(self):
        
        queryset = super().get_queryset()
        queryset = queryset.order_by('-created_at')
        
        return queryset


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field='slug'

    
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    filter_backends=[SearchFilter, OrderingFilter]
    search_fields=['full_name', 'birth_date']
    pagination_class=StandardResultsPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    
    
class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    permission_classes=[permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field='id'

    


class PromoCodeView(APIView):
    permission_classes = [permissions.IsAuthenticated]   

    def post(self, request):
        serializer = CouponApplySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        coupon = serializer.validated_data['code']  
        request.session['promo_code'] = coupon.code
        request.session['discount_percent'] = float(coupon.discount)

        return Response({
            "message": f"Promo kod qo'llanildi: {coupon.code}",
            "discount": f"{coupon.discount}% chegirma",
            
        }, status=status.HTTP_200_OK)
    


class WishListCreateView(generics.ListCreateAPIView):
    queryset=WishList.objects.all()
    serializer_class=WishListSerializer
    permission_classes=[permissions.IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class=StandardResultsPagination
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    
class WishListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=WishList.objects.all()
    serializer_class=WishListSerializer
    permission_classes=[permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field='slug'

    