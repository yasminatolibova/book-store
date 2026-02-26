from django.contrib import admin

# Register your models here.
from .models import Cart, Cartitem, Order, Orderitem
admin.site.register(Cart)
admin.site.register(Cartitem)
admin.site.register(Order)
admin.site.register(Orderitem)