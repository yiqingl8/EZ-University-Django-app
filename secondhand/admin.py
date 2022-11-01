from django.contrib import admin

from .models import Cart, Cartitem, Category, Product, User, Order, Orderitem, Address

admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Cartitem)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Orderitem)
admin.site.register(Address)


