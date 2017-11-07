from django.views.generic import ListView, DetailView, View
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render

from .models import Product


class ProductDetails(DetailView):
    template_name = "products/products_details.html"

    # get the object and pass it to the template
    def get_queryset(self):
        product_slug = self.kwargs.get("slug")
        product = Product.objects.filter(slug=product_slug)
        return product

    def get_context_data(self, **kwargs):
        context = super(ProductDetails, self).get_context_data(**kwargs)
        product_slug = self.kwargs.get("slug")
        product = Product.objects.get(slug=product_slug)
        context["title"] = product.name
        context["gender"] = self.kwargs.get("gender")
        context["section"] = product.section
        return context


class ProductSearch(ListView):
    template_name = "products/products_list.html"

    def get_queryset(self, **kwargs):
        gender = self.kwargs.get("gender")
        query = self.request.GET.get("q")
        # every Q represents an option and every | represents the logical operator OR
        products = Product.objects.filter(
            Q(name__icontains=query, gender=gender) |
            Q(section__icontains=query, gender=gender) |
            Q(category__icontains=query, gender=gender)
        ).distinct()  # distinct to avoid duplicates
        return products

    def get_context_data(self, **kwargs):
        context = super(ProductSearch, self).get_context_data(**kwargs)
        gender = self.kwargs.get("gender")
        context["gender"] = gender
        if gender == "Women":
            title = "Busqueda Mujer"
        else:
            title = "Busqueda Hombre"
        context["title"] = title
        return context


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
        category = self.kwargs.get("category")
        if gender == "Women":
            title = str(category) + " Mujer"
        else:
            title = str(category) + " Hombre"
        context["title"] = title
        return context


class IndexView(View):

    def get(self, request, **kwargs):
        template_name = "products/index.html"
        gender = kwargs.get("gender")
        if gender == "Women":
            title = "Moda Mujer"
        else:
            title = "Moda Hombre"
        context = {
            "gender": gender,
            "title": title,
        }
        return render(request, template_name, context)
