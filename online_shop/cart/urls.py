from django.urls import path

from .views import *

app_name = 'cart'

urlpatterns = [
    path('add/<product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<product_id>/', remove_from_cart, name='remove_from_cart'),
    path('list/', show_cart, name='show_cart'),
]
