from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey
from .fields import OrderField

# Create your models here.


# How to create a custom manager
# class ActiveManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_active=True)


class Category(MPTTModel):
    name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2), MaxLengthValidator(50)],
        null=False,
        blank=False,
        unique=True,
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2), MaxLengthValidator(50)],
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2), MaxLengthValidator(50)],
        null=False,
        blank=False,
        unique=True,
    )
    slug = models.SlugField(unique=True, editable=False, blank=True)
    description = models.TextField(
        max_length=500,
        validators=[MinLengthValidator(10), MaxLengthValidator(500)],
        null=True,
        blank=True,
    )
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug


class ProductLine(models.Model):
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
    )
    sku = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(1), MaxLengthValidator(100)],
    )
    stock_qty = models.PositiveIntegerField(null=False, blank=False, default=0)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product_line",
    )
    is_active = models.BooleanField(default=True)
    order = OrderField(blank=True, unique_for_field="product")

    def __str__(self):
        return str(self.product)
