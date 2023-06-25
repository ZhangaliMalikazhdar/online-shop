from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from shop.models import *
from .forms import *


# crud Category Product
class ListCategory(ListView):
    model = Category
    context_object_name = 'categories'
    # print(category.products)

    def get_queryset(self):
        return Category.objects.order_by('name')


class ListProduct(ListView):
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.order_by('category')


class CreateCategory(CreateView):
    model = Category
    fields = ['name', 'slug']
    template_name = 'create-category.html'

    success_url = '/manager/'
    # def get_success_url(self):
    #     return redirect('manager:list-category')


class EditCategory(UpdateView):
    model = Category
    fields = ['name', 'slug']
    template_name = 'edit-category.html'

    success_url = '/manager/'
    # def get_success_url(self):
    #     return redirect('/')


class DeleteCategory(DeleteView):
    model = Category
    template_name = 'delete-category.html'
    success_url = reverse_lazy('manager:list-category')


class CreateProduct(CreateView):
    model = Product
    fields = ['name', 'image', 'description', 'price', 'slug', 'category']
    # form_class = CreateProductForm
    template_name = 'create-product.html'
    
    # def form_valid(self, form):
    #     image = form.cleaned_data['image']
    #     return super().form_valid(form)

    # def get_success_url(self):
    #     return redirect('manager:create-product.html')


class EditProduct(UpdateView):
    model = Product
    fields = ['name', 'slug', 'description', 'image', 'price', 'category']
    template_name = 'edit-product.html'

    
class DeleteProduct(DeleteView):
    model = Product
    success_url = reverse_lazy('manager:list-product')
    template_name = 'delete-product.html'
