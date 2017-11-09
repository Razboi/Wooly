from django.db import models
from django.contrib.auth import get_user_model

from apps.products.models import Product

User = get_user_model()


class CartProduct(models.Model):
    product = models.ForeignKey(Product)
    user = models.ForeignKey(User)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.product.name + " | " + self.user.username
