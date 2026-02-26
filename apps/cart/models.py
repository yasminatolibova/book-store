from django.db import models
from django.conf import settings
# Create your models here.
from ..book.models import Book
from ..accounts.models import User
from django.core.validators import MinValueValidator

class Cart(models.Model):
    user= models. ForeignKey(User, on_delete=models.CASCADE, related_name='cart', blank=True, null=True)
     created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField()
    is_active=models.BooleanField(default=True)

    def __str__(self):
    
           return f"{self.user.username}"
        
    def get_total_items(self):
        return self.items.aggregate(total=models.Sum('quantity'))['total'] or 0
    
    def get_total_price(self):
        return sum(item.get_subtotal() for item in self.items.all())
    
class Cartitem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitem')
    book=models.ForeignKey(Book, on_delete=models.CASCADE, related_name='cart_item')
    quantity=models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    add_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=['cart', 'book']

    def __str__(self):
        return f"{self.quantity}*{self.book.title}"
    
    def get_subtotal(self):
        return self.quantity*self.book.price
    


class Order(models.Model):
    user= models. ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    status=models.CharField(max_length=100)
    total_amount=models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    address=models.CharField()
    phone=models.IntegerField()
    PAYMENT_METHOD= [
        ("cash", "Cash"),
        ("card", "Card"),
        ("check", "Check")
    ]
    payment_method=models.CharField(max_length=20, choices=PAYMENT_METHOD, default='card')


    def __str__(self):
        return f"{self.user}"
    

class Orderitem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    book=models.ForeignKey(Book, on_delete=models.CASCADE, related_name='orderitem')
    quantity=models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    unit_price=models.DecimalField(max_digits=10, decimal_places=2)

        
    def __str__(self):
        return f"{self.book.title}--{self.unit_price}dan"
    
    def get_subtotal(self):
        return  self.quantity*self.unit_price









