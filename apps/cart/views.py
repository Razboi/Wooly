from django.shortcuts import redirect
from django.views.generic import View, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.products.models import Product
from .models import CartProduct


class AddToCart(LoginRequiredMixin, View):

    def post(self, request, **kwargs):
        user = self.request.user
        product_pk = self.kwargs.get("pk")
        product = Product.objects.get(pk=product_pk)
        size = request.POST["sizes"]
        cart_p = CartProduct(product=product, user=user, size=size)
        cart_p.save()
        return redirect("products:index", gender="Women")
