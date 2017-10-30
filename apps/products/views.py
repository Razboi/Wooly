from django.shortcuts import reverse
from django.views.generic import ListView, View

from .models import Product


class ProductsList(ListView):
    template_name = "products/products_list.html"

    def get_queryset(self):
        return Product.objects.all()


class IndexView(ListView):
    template_name = "products/index.html"

    def get_queryset(self):
        return None

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        gender = self.kwargs.get("gender")
        context["gender"] = gender
        if gender == "women":
            title = "Moda Mujer"
        else:
            title = "Moda Hombre"
        context["title"] = title
        return context
