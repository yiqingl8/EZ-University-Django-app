from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from secondhand.form import CategoryForm, AddressForm, ProductForm, UserForm, CartForm, CartItemForm, OrderForm, \
    OrderItemForm
from secondhand.models import Product, Order, Cart, Cartitem, Orderitem, User, Address, Category
from secondhand.utils import PageLinksMixin


class ProductList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 20
    model = Product
    permission_required = 'secondhand.view_product'

class ProductDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Product
    permission_required = 'secondhand.view_product'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        product = self.get_object()
        seller = product.seller
        category = product.category
        context['category'] = category
        context['seller'] = seller
        return context

class ProductCreate(CreateView):
    form_class = ProductForm
    model = Product
    permission_required = 'secondhand.add_product'

class ProductUpdate(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'secondhand/product_form_update.html'
    permission_required = 'secondhand.change_product'

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('secondhand_product_list_urlpattern')
    permission_required = 'secondhand.delete_product'

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        cartitems = product.cartitems.all()
        orderitems = product.orderitems.all()
        if cartitems.count() > 0 or orderitems.count() > 0:
            return render(
                request,
                'secondhand/product_refuse_delete.html',
                {'product': product,
                 'cartitems': cartitems,
                 'orderitems': orderitems
                 }
            )
        else:
            return render(
                request,
                'secondhand/product_confirm_delete.html',
                {'product': product}
            )


class UserList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = User
    permission_required = 'secondhand.view_user'

class UserDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = User
    permission_required = 'secondhand.view_user'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        user = self.get_object()
        cart_list = user.carts.all()
        order_list = user.orders.all()
        product_list = user.products.all()
        context['cart_list'] = cart_list
        context['order_list'] = order_list
        context['product_list'] = product_list
        return context

class UserCreate(CreateView):
    form_class = UserForm
    model = User
    permission_required = 'secondhand.add_user'

class UserUpdate(UpdateView):
    form_class = UserForm
    model = User
    template_name = 'secondhand/user_form_update.html'
    permission_required = 'secondhand.change_user'

class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('secondhand_user_list_urlpattern')
    permission_required = 'secondhand.delete_user'

    def get(self, request, pk):
        users = get_object_or_404(User, pk=pk)
        products = users.products.all()
        carts = users.carts.all()
        orders = users.orders.all()
        if products.count() > 0 or orders.count() > 0 or carts.count() > 0:
            return render(
                request,
                'secondhand/user_refuse_delete.html',
                {'user': users,
                 'products': products,
                 'orders': orders,
                 'carts': carts
                 }
            )
        else:
            return render(
                request,
                'secondhand/user_confirm_delete.html',
                {'user': users}
            )


class CartList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 15
    model = Cart
    permission_required = 'secondhand.view_cart'


class CartDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Cart
    permission_required = 'secondhand.view_cart'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        cart = self.get_object()
        cartitem_list = cart.cartitems.all()
        user = cart.user
        context['cartitem_list'] = cartitem_list
        context['user'] = user
        return context

class CartCreate(CreateView):
    form_class = CartForm
    model = Cart
    permission_required = 'secondhand.add_cart'


class CartUpdate(UpdateView):
    form_class = CartForm
    model = Cart
    template_name = 'secondhand/cart_form_update.html'
    permission_required = 'secondhand.change_cart'


class CartDelete(DeleteView):
    model = Cart
    success_url = reverse_lazy('secondhand_cart_list_urlpattern')
    permission_required = 'secondhand.delete_cart'

    def get(self, request, pk):
        cart = get_object_or_404(Cart, pk=pk)
        cartitems = cart.cartitems.all()
        if cartitems.count() > 0:
            return render(
                    request,
                    'secondhand/cart_refuse_delete.html',
                    {'cart': cart,
                     'cartitems': cartitems,
                     }
                )
        else:
            return render(
                    request,
                    'secondhand/cart_confirm_delete.html',
                    {'cart': cart}
                )

class CartItemList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Cartitem
    permission_required = 'secondhand.view_cartitem'


class CartItemDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Cartitem
    permission_required = 'secondhand.view_cartitem'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        cartitem = self.get_object()
        cart = cartitem.cart
        item = cartitem.product
        context['cart'] = cart
        context['item'] = item
        return context

class CartItemCreate(CreateView):
    form_class = CartItemForm
    model = Cartitem
    permission_required = 'secondhand.add_cartitem'


class CartItemUpdate(UpdateView):
    form_class = CartItemForm
    model = Cartitem
    template_name = 'secondhand/cartitem_form_update.html'
    permission_required = 'secondhand.change_cartitem'


class CartItemDelete(DeleteView):
    model = Cartitem
    success_url = reverse_lazy('secondhand_cartitem_list_urlpattern')
    permission_required = 'secondhand.delete_cartitem'

class OrderList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Order
    permission_required = 'secondhand.view_order'

class OrderDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Order
    permission_required = 'secondhand.view_order'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        order = self.get_object()
        orderitem_list = order.orderitems.all()
        address_list = order.address.all()
        user = order.user
        context['orderitem_list'] = orderitem_list
        context['address_list'] = address_list
        context['user'] = user
        return context

class OrderCreate(CreateView):
    form_class = OrderForm
    model = Order
    permission_required = 'secondhand.add_order'

class OrderUpdate(UpdateView):
    form_class = OrderForm
    model = Order
    template_name = 'secondhand/order_form_update.html'
    permission_required = 'secondhand.change_order'

class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('secondhand_order_list_urlpattern')
    permission_required = 'secondhand.delete_order'

    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        orderitems = order.orderitems.all()
        addresses = order.address.all()
        if orderitems.count() > 0:
            return render(
                request,
                'secondhand/order_refuse_delete.html',
                {'order': order,
                 'orderitems': orderitems,
                 }
            )
        elif addresses.count() > 0:
            return render(
                request,
                'secondhand/order_refuse_delete.html',
                {'order': order,
                 'addresses': addresses,
                 }
            )
        else:
            return render(
                request,
                'secondhand/order_confirm_delete.html',
                {'order': order}
            )


class OrderItemList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Orderitem
    permission_required = 'secondhand.view_orderitem'


class OrderItemDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Orderitem
    permission_required = 'secondhand.view_orderitem'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        orderitem = self.get_object()
        context['order'] = orderitem.order
        context['item'] = orderitem.item
        return context

class OrderItemCreate(CreateView):
    form_class = OrderItemForm
    model = Orderitem
    permission_required = 'secondhand.add_orderitem'

class OrderItemUpdate(UpdateView):
    form_class = OrderItemForm
    model = Orderitem
    template_name = 'secondhand/orderitem_form_update.html'
    permission_required = 'secondhand.change_orderitem'

class OrderItemDelete(DeleteView):
    model = Orderitem
    success_url = reverse_lazy('secondhand_orderitem_list_urlpattern')
    permission_required = 'secondhand.delete_orderitem'

class AddressList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Address
    permission_required = 'secondhand.view_address'


class AddressDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Address
    permission_required = 'secondhand.view_address'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        address = self.get_object()
        order = address.order
        context['order'] = order
        return context

class AddressCreate(CreateView):
    form_class = AddressForm
    model = Address
    permission_required = 'secondhand.add_address'

class AddressUpdate(UpdateView):
    form_class = AddressForm
    model = Address
    template_name = 'secondhand/address_form_update.html'
    permission_required = 'secondhand.change_address'

class AddressDelete(DeleteView):
    model = Address
    success_url = reverse_lazy('secondhand_address_list_urlpattern')
    permission_required = 'secondhand.delete_address'


class CategoryList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Category
    permission_required = 'secondhand.view_category'

class CategoryDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Category
    permission_required = 'secondhand.view_category'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        category = self.get_object()
        product_list = category.products.all()
        context['product_list'] = product_list
        return context

class CategoryCreate(CreateView):
    form_class = CategoryForm
    model = Category
    permission_required = 'secondhand.add_category'

class CategoryUpdate(UpdateView):
    form_class = CategoryForm
    model = Category
    template_name = 'secondhand/category_form_update.html'
    permission_required = 'secondhand.change_category'

class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('secondhand_category_list_urlpattern')
    permission_required = 'secondhand.delete_category'

    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        products = category.products.all()
        if products.count() > 0:
            return render(
                    request,
                    'secondhand/category_refuse_delete.html',
                    {'category': category,
                     'products': products
                     }
                )
        else:
            return render(
                    request,
                    'secondhand/category_confirm_delete.html',
                    {'category': category}
                )
