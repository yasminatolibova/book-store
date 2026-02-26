from django.urls import path
from .views import (CartListCreateView, 
                    CartDetailView, 
                    CartitemListCreateView, 
                    CartitemDetailView, 
                    OrderListCreateView, 
                    OrderDetailView,
                    checkout_cart)
urlpatterns=[
    path('carts/', CartListCreateView.as_view(), name='carts'),
    path('carts/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
    path('cartitems/', CartitemListCreateView.as_view(), name='cartitems'),
    path('cartitems/<int:pk>/', CartitemDetailView.as_view(), name='cartitem-detail'),
    path('orders/', OrderListCreateView.as_view(), name='orders'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('carts/<int:cart_id>/chechkout/', checkout_cart, name='cart-checkot')
]