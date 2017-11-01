from django.shortcuts import reverse
from django.views.generic import ListView, View

from .models import Product


class ProductsList(ListView):
    template_name = "products/products_list.html"

    def get_queryset(self, **kwargs):
        gender = self.kwargs.get("gender")
        category = self.kwargs.get("category")
        sections = ["Prendas", "Calzado", "Complementos"]
        # if the category is a section return all the products for that section
        for i in sections:
            if i == category:
                products = Product.objects.filter(gender=gender, section=i)
                return products
        # if the category is novedades return the new products, same with ofertas/discounted products
        if category == "Novedades":
            products = Product.objects.filter(gender=gender, new=True)
        elif category == "Ofertas":
            products = Product.objects.filter(gender=gender, discounted=True)
        # else return the products in the category
        else:
            products = Product.objects.filter(gender=gender, category=category)
        return products

    def get_context_data(self, **kwargs):
        context = super(ProductsList, self).get_context_data(**kwargs)
        gender = self.kwargs.get("gender")
        context["gender"] = gender
        print(gender)
        category = self.kwargs.get("category")
        if gender == "Women":
            title = str(category) + " Mujer"
        else:
            title = str(category) + " Hombre"
        context["title"] = title
        return context


class IndexView(ListView):
    template_name = "products/index.html"

    def get_queryset(self):
        return None

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        gender = self.kwargs.get("gender")
        context["gender"] = gender
        if gender == "Women":
            title = "Moda Mujer"
        else:
            title = "Moda Hombre"
        context["title"] = title
        return context
