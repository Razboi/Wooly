import json

from django.shortcuts import redirect, get_object_or_404, reverse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.http import HttpResponse

from apps.products.models import Product
from .models import CartProduct


class AddToCart(LoginRequiredMixin, View):

    def get(self, request, **kwargs):
        product_pk = self.kwargs.get("pk")
        product = Product.objects.get(pk=product_pk)
        return redirect(product.get_absolute_url())

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
    def post(self, request, **kwargs):
        cart_pk = request.POST["pk"]
        cart = get_object_or_404(CartProduct, user=self.request.user, pk=cart_pk)
        cart.delete()

        data = ""
        return HttpResponse(json.dumps(data), content_type="application/json")
