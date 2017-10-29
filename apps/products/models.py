from django.db import models
from django.db.models.signals import pre_save

from utils.unique_slug_generator import unique_slug_generator


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=5000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)  # needs pillow
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    discounted = models.BooleanField(default=False)
    discounted_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, max_length=170)

    abrigos = "Abr"
    accesorios = "Acc"
    americanas = "Ame"
    basicos = "Bas"
    botas = "Bot"
    camisas = "Cam"
    jerseis = "Jer"
    pantalones = "Pan"
    sudaderas = "Sud"
    vaqueros = "Vaq"
    zapatillas = "Zap"

    category_choices = (
        (abrigos, "Abrigos"),
        (accesorios, "Accesorios"),
        (americanas, "Americanas"),
        (basicos, "Basicos"),
        (botas, "Botas"),
        (camisas, "Camisas"),
        (jerseis, "Jerseis"),
        (pantalones, "Pantalones"),
        (sudaderas, "Sudaderas"),
        (vaqueros, "Vaqueros"),
        (zapatillas, "Zapatillas"),
    )

    category = models.CharField(max_length=20, choices=category_choices, null=True)

    def __str__(self):
        return self.name


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender=Product)
