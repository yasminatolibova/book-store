from django.urls import path
from .views import CategoryListCreateView, CategoryDetailView, BookDetailView, BookListCreateView, AuthorListCreateView, AuthorDetailView, PromoCodeView

urlpatterns=[
    path('categories/', CategoryListCreateView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('books/', BookListCreateView.as_view(), name='books'),
    path('books/<slug:slug>/', BookDetailView.as_view(), name='book-detail'),
    path('authors/', AuthorListCreateView.as_view(), name='authors'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('coupons/', PromoCodeView.as_view(), name='code')
]