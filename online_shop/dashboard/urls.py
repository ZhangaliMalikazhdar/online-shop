from django.urls import path

from .views import *

app_name = 'dashboard'

urlpatterns = [
    path('products', products, name='products'),
    path('products/delete/<int:pk>', delete_product, name='delete_product'),
    path('products/edit/<int:pk>', edit_product, name='edit_product'),
    path('orders', orders, name='orders'),
    path('orders/detail/<int:pk>', order_detail, name='order_detail'),
    path('add-product/', add_product, name='add_product'),
    path('add-category/', add_category, name='add_category'),
]
