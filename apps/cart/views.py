from django.shortcuts import redirect, get_object_or_404, reverse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F

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
        product_qs = CartProduct.objects.filter(product=product, user=user, size=size)
        # if the product already exists (same size) increment one unit, else add the product
        if product_qs.exists():
            product_qs.update(quantity=F("quantity") + 1)  # F is used to increment/decrement a model field
        else:
            cart_p = CartProduct(product=product, user=user, size=size)
            cart_p.save()

        gender = product.gender
        category = product.category
        return redirect("products:category", gender=gender, category=category)


class CartDelete(LoginRequiredMixin, View):

    def get(self, request, **kwargs):
        cart_pk = self.kwargs.get("pk")
        cart = get_object_or_404(CartProduct, user=self.request.user, pk=cart_pk)
        # if the quantity of the product is > 1 decrement one unit, else delete the product
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
        else:
            cart.delete()
        return redirect("products:category", gender=cart.product.gender, category=cart.product.category)


