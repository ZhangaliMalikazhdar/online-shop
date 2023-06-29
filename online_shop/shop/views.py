from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Product, Category
from cart.forms import QuantityForm


def pagination(request, list_objects):
    paginator = Paginator(list_objects, 20)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


def home_page(request):
    products = Product.objects.all()
    context = {'products': pagination(request, products)}
    return render(request, 'home_page.html', context)


def product_detail(request, pk):
    form = QuantityForm()
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category).all()[:5]
    context = {
        'name': product.name,
        'product': product,
        'form': form,
        'favorites': 'favorites',
        'related_products': related_products
    }
    if request.user.likes.filter(pk=product.pk).first():
        context['favorites'] = 'remove'
    return render(request, 'product_detail.html', context)


@login_required
def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    request.user.likes.add(product)
    return redirect('shop:product_detail', pk=product.pk)


@login_required
def remove_from_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    request.user.likes.remove(product)
    return redirect('shop:favorites')


@login_required
def favorites(request):
    products = request.user.likes.all()
    context = {'title': 'Favorites', 'products': products}
    return render(request, 'favorites.html', context)


def search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query).all()
    context = {'products': pagination(request, products)}
    return render(request, 'home_page.html', context)


def filter_by_category(request, pk):
    result = []
    category = Category.objects.filter(pk=pk).first()
    [result.append(product)
        for product in Product.objects.filter(category=category.id).all()]

    context = {'products': pagination(request, result)}
    return render(request, 'home_page.html', context)
