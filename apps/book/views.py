from django.shortcuts import render

# Create your views here.
from .models import Category, Author, Book
from rest_framework import permissions,  generics
from rest_framework.response import Response
from .serializers import CategorySerializer, AuthorSerializer, BookSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view



class CategoryListCreateView(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookListCreateView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    filter_backends=[SearchFilter, OrderingFilter]
    search_fields=['title', 'author', 'category', 'isbn']
    ordering_fileds=['language', 'stock']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field='slug'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    filter_backends=[SearchFilter, OrderingFilter]
    search_fields=['full_name', 'birth_date']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    
    
class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    permission_classes=[permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field='id'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

