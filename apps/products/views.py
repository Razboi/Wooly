from django.views.generic import ListView
from django.db.models import Q

from .models import Product


class ProductSearch(ListView):
    template_name = "products/products_list.html"

    def get_queryset(self, **kwargs):
        gender = self.kwargs.get("gender")
        query = self.request.GET.get("q")
        print(query)
        products = Product.objects.filter(
            Q(name__icontains=query, gender=gender) |
            Q(section__icontains=query, gender=gender) |
            Q(category__icontains=query, gender=gender)
        ).distinct()
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
