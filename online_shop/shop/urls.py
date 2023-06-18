from django.urls import path

from .views import *

app_name = 'shop'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('<slug:slug>', product_detail, name='product_detail'),
    path('add/favorites/<int:product_id>/', add_to_favorites, name='add_to_favorites'),
    path('remove/favorites/<int:product_id>/', remove_from_favorites, name='remove_from_favorites'),
    path('favorites/', favorites, name='favorites'),
    path('search/', search, name='search'),
    path('filter/<slug:slug>/', filter_by_category, name='filter_by_category')
]
