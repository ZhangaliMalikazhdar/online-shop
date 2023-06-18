from django.urls import path

from .views import *

app_name = "orders"

urlpatterns = [
    path('create', create_order, name='create_order'),
    path('list', user_orders, name='user_orders'),
    path('checkout/<int:order_id>', checkout, name='checkout'),
    path('fake-payment/<int:order_id>', fake_payment, name='pay_order')
]
