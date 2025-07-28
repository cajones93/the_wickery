from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Scent(models.Model):
    """
    Model for different scent options for products.
    """
    name = models.CharField(max_length=100, unique=True)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class WaxType(models.Model):
    """
    Model for different wax types for products.
    """
    class Meta:
        verbose_name_plural = 'Wax Types'

    name = models.CharField(max_length=100, unique=True)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)
    price_modifier = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, default=1.00,)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class CandleSize(models.Model):
    """
    Model for different wax types for products.
    """
    name = models.CharField(max_length=100, unique=True)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)
    price_modifier = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, default=1.00,)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name if self.friendly_name else self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    has_scents = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=1, null=True, blank=True, validators=[
            MinValueValidator(1, message='Rating must be at least 1.'),
            MaxValueValidator(5, message='Rating cannot exceed 5.')
        ])
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    available_scents = models.ManyToManyField(Scent, blank=True, related_name='products_available_scents')
    available_wax_types = models.ManyToManyField(WaxType, blank=False, related_name='products_available_wax_types')
    available_sizes = models.ManyToManyField(CandleSize, blank=True, related_name='products_available_sizes')

    def __str__(self):
        return self.name
