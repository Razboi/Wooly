from django.db import models
from django.db.models.signals import pre_save

from utils.unique_slug_generator import unique_slug_generator


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=5000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)  # needs pillow
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    discounted = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    discounted_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, max_length=170)

    # Product sections
    PRENDAS = "Prendas"
    CALZADO = "Calzado"
    COMPLEMENTOS = "Complementos"
    section_choices = (
        (PRENDAS, "Prendas"),
        (CALZADO, "Calzado"),
        (COMPLEMENTOS, "Complementos"),
    )
    section = models.CharField(max_length=20, choices=section_choices, default=PRENDAS)

    # Product categories
    ABRIGOS = "Abrigos"
    CHAQUETAS = "Chaquetas"
    AMERICANAS = "Americanas"
    CAMISETAS = "Camisetas"
    CAMISAS = "Camisas"
    JERSEIS = "Jerseis"
    PANTALONES = "Pantalones"
    SUDADERAS = "Sudaderas"
    ZAPATOS = "Zapatos"
    MOCASINES = "Mocasines"
    BOTAS = "Botas"
    DEPORTIVAS = "Deportivas"
    CINTURONES = "Cinturones"
    BUFANDAS = "Bufandas"
    GORROS = "Gorros"
    CORBATAS = "Corbatas"
    category_choices = (
        (ABRIGOS, "Abrigos"),
        (CHAQUETAS, "Chaquetas"),
        (AMERICANAS, "Americanas"),
        (CAMISETAS, "Camisetas"),
        (CAMISAS, "Camisas"),
        (JERSEIS, "Jerseis"),
        (PANTALONES, "Pantalones"),
        (SUDADERAS, "Sudaderas"),
        (ZAPATOS, "Zapatos"),
        (MOCASINES, "Mocasines"),
        (BOTAS, "Botas"),
        (DEPORTIVAS, "Deportivas"),
        (CINTURONES, "Cinturones"),
        (BUFANDAS, "Bufandas"),
        (GORROS, "Gorros"),
        (CORBATAS, "Corbatas"),
    )
    category = models.CharField(max_length=20, choices=category_choices, null=True)

    # Gender Categories
    MEN = "Men"
    WOMEN = "Women"
    category_choices = (
        (MEN, "Men"),
        (WOMEN, "Women"),
    )
    gender = models.CharField(max_length=20, choices=category_choices, null=True)

    def __str__(self):
        description = self.name + " | " + self.gender + " |D " + str(self.discounted) + " |N " + \
                      str(self.new)
        return description


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender=Product)
