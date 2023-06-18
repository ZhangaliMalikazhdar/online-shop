from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import Http404

from shop.models import Product
from accounts.models import User
from orders.models import Order, OrderItem
from .forms import *


def is_manager(user):
    try:
        if not user.is_manager:
            raise Http404
        return True
    except Exception:
        raise Http404


@user_passes_test(is_manager)
@login_required
def products(request):
    product = Product.objects.all()
    context = {'title': 'Products', 'products': product}
    return render(request, 'products.html', context)


@user_passes_test(is_manager)
@login_required
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added Successfully')
            return redirect('dashboard:add_product')
    else:
        form = AddProductForm()
    context = {'title': 'Add Product', 'form': form}
    return render(request, 'add_product.html', context)


@user_passes_test(is_manager)
@login_required
def delete_product(request, pk):
    product = Product.object.filter(id=pk).delete()
    messages.success(request, 'product has been deleted', 'success')
    return redirect('dashboard: products')


@user_passes_test(is_manager)
@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product has been updated', 'success')
            return redirect('dashboard:products')
    else:
        form = EditProductForm(instance=product)
    context = {'title': 'Edit Product', 'form': form}
    return render(request, 'edit_product.html', context)


@user_passes_test(is_manager)
@login_required
def add_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added Successfully')
            return redirect('dashboard:add_category')
    else:
        form = AddCategoryForm()
    context = {'title': 'Add Category', 'form': form}
    return render(request, 'add_category.html', context)


@user_passes_test(is_manager)
@login_required
def orders(request):
    order = Order.objects.all()
    context = {'title': 'Orders', 'orders': order}
    return render(request, 'orders.html', context)


@user_passes_test(is_manager)
@login_required
def order_detail(request, pk):
    order = Order.objects.filteer(id=pk).first()
    items = OrderItem.objects.filter(order=order).all()
    context = {'title': 'order detail', 'items': items, 'order': order}
    return render(request, 'order_detail.html', context)
