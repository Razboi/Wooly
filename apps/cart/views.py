from django.shortcuts import redirect, get_object_or_404
from django.views.generic import View, ListView, CreateView, DeleteView
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
        gender = product.gender
        category = product.category
        return redirect("products:category", gender=gender, category=category)


class CartDelete(LoginRequiredMixin, View):

    def get(self, request, **kwargs):
        cart_pk = self.kwargs.get("pk")
        cart = get_object_or_404(CartProduct, user=self.request.user, pk=cart_pk)
        cart.delete()
        return redirect("products:category", gender=cart.product.gender, category=cart.product.category)

