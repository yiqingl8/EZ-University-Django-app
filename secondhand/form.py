from django import forms

from secondhand.models import Address, Category, User, Product, Cart, Cartitem, Order, Orderitem


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def clean_category_number(self):
        return self.cleaned_data['category_number'].strip()

    def clean_category_name(self):
        return self.cleaned_data['category_name'].strip()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_account(self):
        return self.cleaned_data['account'].strip()

    def clean_password(self):
        return self.cleaned_data['password'].strip()


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_product_name(self):
        return self.cleaned_data['product_name'].strip()

    def clean_product_description(self):
        return self.cleaned_data['product_description'].strip()

    def clean_product_price(self):
        return self.cleaned_data['product_price'].strip()

    def clean_product_color(self):
        return self.cleaned_data['product_color'].strip()

    def clean_product_size(self):
        return self.cleaned_data['product_size'].strip()


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def clean_order_date(self):
        return self.cleaned_data['order_date'].strip()


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = Orderitem
        fields = '__all__'


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

    def clean_name(self):
        return self.cleaned_data['name'].strip()

    def clean_phone(self):
        return self.cleaned_data['phone'].strip()

    def clean_address(self):
        return self.cleaned_data['address'].strip()

    def clean_zip_code(self):
        return self.cleaned_data['ZIP_code'].strip()


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemForm(forms.ModelForm):
    class Meta:
        model = Cartitem
        fields = '__all__'

    def clean_time(self):
        return self.cleaned_data['time'].strip()
