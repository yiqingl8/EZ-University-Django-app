from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_number = models.CharField(max_length=20)
    category_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return f'{self.category_number} - {self.category_name}'

    def get_absolute_url(self):
        return reverse('secondhand_category_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('secondhand_category_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('secondhand_category_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['category_number', 'category_name']
        constraints = [
            UniqueConstraint(fields=['category_number', 'category_name'], name='unique_category')
        ]

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    account = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=45)

    def __str__(self):
        return f'{self.account}'

    def get_absolute_url(self):
        return reverse('secondhand_user_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('secondhand_user_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('secondhand_user_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['first_name', 'last_name', 'account']
        constraints = [
            UniqueConstraint(fields=['first_name', 'last_name', 'account'], name='unique_user')
        ]


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=45, unique=True)
    product_description = models.CharField(max_length=100)
    product_price = models.CharField(max_length=20)
    product_color = models.CharField(max_length=20)
    product_size = models.CharField(max_length=20)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT)
    seller = models.ForeignKey(User, related_name='products', on_delete=models.PROTECT)

    def __str__(self):
        return f' {self.category.category_number}--{self.product_name}--${self.product_price}'

    def get_absolute_url(self):
        return reverse('secondhand_product_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('secondhand_product_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('secondhand_product_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['category', 'product_name', 'seller']
        constraints = [
            UniqueConstraint(fields=['category', 'product_name', 'seller'], name='unique_products')
        ]


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='carts', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.user.account}'

    def get_absolute_url(self):
        return reverse('secondhand_cart_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('secondhand_cart_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('secondhand_cart_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['user', 'cart_id']
        constraints = [
            UniqueConstraint(fields=['user', 'cart_id'], name='unique_cart')
        ]

class Cartitem(models.Model):
    cart_item_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, related_name='cartitems', on_delete=models.PROTECT)
    cart = models.ForeignKey(Cart, related_name='cartitems', on_delete=models.PROTECT)
    time = models.TimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f'{self.cart.cart_id}-{self.product.product_name}'

    def get_absolute_url(self):
        return reverse('secondhand_cartitem_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('secondhand_cartitem_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('secondhand_cartitem_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['cart', 'product', 'time']
        constraints = [
            UniqueConstraint(fields=['cart', 'product', 'time'], name='unique_cartitem')
        ]


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.TimeField(auto_now=True, auto_now_add=False)
    user = models.ForeignKey(User, related_name='orders', on_delete=models.PROTECT)

    def __str__(self):
        return f'order ID: {self.order_id}'

    def get_absolute_url(self):
        return reverse('secondhand_order_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('secondhand_order_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('secondhand_order_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['order_date', 'user']
        constraints = [
            UniqueConstraint(fields=['order_date', 'user'], name='unique_order')
        ]


class Orderitem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Product, related_name='orderitems', on_delete=models.PROTECT)
    order = models.ForeignKey(Order, related_name='orderitems', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.order.order_id}-{self.item.product_name}'

    def get_absolute_url(self):
        return reverse('secondhand_orderitem_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('secondhand_orderitem_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('secondhand_orderitem_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['order', 'item']
        constraints = [
            UniqueConstraint(fields=['order', 'item'], name='unique_orderitem')
        ]


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    ZIP_code = models.CharField(max_length=45)
    order = models.ForeignKey(Order, related_name='address', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.ZIP_code}-{self.name}'

    def get_absolute_url(self):
        return reverse('secondhand_address_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('secondhand_address_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('secondhand_address_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['ZIP_code', 'name']
        constraints = [
            UniqueConstraint(fields=['ZIP_code', 'name'], name='unique_address')
        ]
