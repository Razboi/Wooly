from .models import CartProduct


'''makes the user's cart products available to all the urls so the cart popup can be displayed '''


def cart_products_processor(request):
    if request.user.is_authenticated:
        cart_products = CartProduct.objects.filter(user=request.user)
        return {"cart_products": cart_products}
    return {"cart_products": None}