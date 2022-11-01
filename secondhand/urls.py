from django.urls import path
from secondhand.views import (
    ProductList,
    UserList,
    CartList,
    CartItemList,
    OrderList,
    AddressList,
    OrderItemList, ProductDetail, UserDetail, CartDetail, CartItemDetail, OrderDetail, OrderItemDetail, AddressDetail,
    CategoryList, CategoryDetail, ProductCreate, UserCreate, CartCreate, CartItemCreate, OrderCreate, OrderItemCreate,
    AddressCreate, CategoryCreate, ProductUpdate, UserUpdate, CartUpdate, CartItemUpdate, OrderUpdate, OrderItemUpdate,
    AddressUpdate, CategoryUpdate, ProductDelete, CartDelete, OrderDelete, OrderItemDelete, AddressDelete,
    CategoryDelete, CartItemDelete, UserDelete

)


urlpatterns = [

    path('product/',
         ProductList.as_view(),
         name='secondhand_product_list_urlpattern'),

    path('product/<int:pk>/',
         ProductDetail.as_view(),
         name='secondhand_product_detail_urlpattern'),

    path('product/<int:pk>/update/',
         ProductUpdate.as_view(),
         name='secondhand_product_update_urlpattern'),

    path('product/create/',
         ProductCreate.as_view(),
         name='secondhand_product_create_urlpattern'),

    path('product/<int:pk>/delete/',
         ProductDelete.as_view(),
         name='secondhand_product_delete_urlpattern'),

    path('user/',
         UserList.as_view(),
         name='secondhand_user_list_urlpattern'),

    path('user/<int:pk>/',
         UserDetail.as_view(),
         name='secondhand_user_detail_urlpattern'),

    path('user/create/',
         UserCreate.as_view(),
         name='secondhand_user_create_urlpattern'),

    path('user/<int:pk>/update/',
         UserUpdate.as_view(),
         name='secondhand_user_update_urlpattern'),

    path('user/<int:pk>/delete/',
         UserDelete.as_view(),
         name='secondhand_user_delete_urlpattern'),

    path('cart/',
         CartList.as_view(),
         name='secondhand_cart_list_urlpattern'),

    path('cart/<int:pk>/',
         CartDetail.as_view(),
         name='secondhand_cart_detail_urlpattern'),

    path('cart/create/',
         CartCreate.as_view(),
         name='secondhand_cart_create_urlpattern'),

    path('cart/<int:pk>/update/',
         CartUpdate.as_view(),
         name='secondhand_cart_update_urlpattern'),

    path('cart/<int:pk>/delete/',
         CartDelete.as_view(),
         name='secondhand_cart_delete_urlpattern'),

    path('cartitem/',
         CartItemList.as_view(),
         name='secondhand_cartitem_list_urlpattern'),

    path('cartitem/<int:pk>/',
         CartItemDetail.as_view(),
         name='secondhand_cartitem_detail_urlpattern'),

    path('cartitem/create/',
         CartItemCreate.as_view(),
         name='secondhand_cartitem_create_urlpattern'),

    path('cartitem/<int:pk>/update/',
         CartItemUpdate.as_view(),
         name='secondhand_cartitem_update_urlpattern'),

    path('cartitem/<int:pk>/delete/',
         CartItemDelete.as_view(),
         name='secondhand_cartitem_delete_urlpattern'),

    path('order/',
         OrderList.as_view(),
         name='secondhand_order_list_urlpattern'),

    path('order/<int:pk>/',
         OrderDetail.as_view(),
         name='secondhand_order_detail_urlpattern'),

    path('order/create/',
         OrderCreate.as_view(),
         name='secondhand_order_create_urlpattern'),

    path('order/<int:pk>/update/',
         OrderUpdate.as_view(),
         name='secondhand_order_update_urlpattern'),

    path('order/<int:pk>/delete/',
         OrderDelete.as_view(),
         name='secondhand_order_delete_urlpattern'),

    path('orderitem/',
         OrderItemList.as_view(),
         name='secondhand_orderitem_list_urlpattern'),

    path('orderitem/<int:pk>/',
         OrderItemDetail.as_view(),
         name='secondhand_orderitem_detail_urlpattern'),

    path('orderitem/create/',
         OrderItemCreate.as_view(),
         name='secondhand_orderitem_create_urlpattern'),

    path('orderitem/<int:pk>/update/',
         OrderItemUpdate.as_view(),
         name='secondhand_orderitem_update_urlpattern'),

    path('orderitem/<int:pk>/delete/',
         OrderItemDelete.as_view(),
         name='secondhand_orderitem_delete_urlpattern'),

    path('address/',
         AddressList.as_view(),
         name='secondhand_address_list_urlpattern'),

    path('address/<int:pk>/',
         AddressDetail.as_view(),
         name='secondhand_address_detail_urlpattern'),

    path('address/create/',
         AddressCreate.as_view(),
         name='secondhand_address_create_urlpattern'),

    path('address/<int:pk>/update/',
         AddressUpdate.as_view(),
         name='secondhand_address_update_urlpattern'),

    path('address/<int:pk>/delete/',
         AddressDelete.as_view(),
         name='secondhand_address_delete_urlpattern'),

    path('category/',
         CategoryList.as_view(),
         name='secondhand_category_list_urlpattern'),

    path('category/<int:pk>/',
         CategoryDetail.as_view(),
         name='secondhand_category_detail_urlpattern'),

    path('category/create/',
         CategoryCreate.as_view(),
         name='secondhand_category_create_urlpattern'),

    path('category/<int:pk>/update/',
         CategoryUpdate.as_view(),
         name='secondhand_category_update_urlpattern'),

    path('category/<int:pk>/delete/',
         CategoryDelete.as_view(),
         name='secondhand_category_delete_urlpattern'),
]
