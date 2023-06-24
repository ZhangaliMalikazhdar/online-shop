from django.urls import path

from .views import *

app_name = 'manager'

urlpatterns = [
    path('', ListCategory.as_view(template_name='list-category.html'), name='list-category'),
    path('product/', ListProduct.as_view(template_name='list-product.html'), name='list-product'),
    path('create-category/', CreateCategory.as_view(), name='create-category'),
    path('create-product/', CreateProduct.as_view(), name='create-product'),
    path('<int:pk>/edit-category/', EditCategory.as_view(), name='edit-category'),
    path('<int:pk>/delete-category/', DeleteCategory.as_view(), name='delete-category'),
    path('<int:pk>/edit-product/', EditProduct.as_view(), name='edit-product'),
    path('<int:pk>/delete-product/', DeleteProduct.as_view(), name='delete-product'),
]
