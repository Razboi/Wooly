from django.shortcuts import render
from django.views.generic import ListView

from .models import Product


class ProductsList(ListView):
    template_name = "products/products_list.html"

    def get_queryset(self):
        return Product.objects.all()
