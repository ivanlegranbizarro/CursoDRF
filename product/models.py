from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey


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
    order = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["product", "order"],
                name="unique_order_for_product",
            )
        ]

    def save(self, *args, **kwargs):
        if self.order is None:
            max_order = ProductLine.objects.filter(product=self.product).aggregate
            (models.Max("order"))["order__max"]

            self.order = (max_order or 0) + 1

            super().save(*args, **kwargs)

    def __str__(self):
        return str(self.product)


class ProductImage(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2), MaxLengthValidator(100)],
        null=False,
        blank=False,
    )
    alternative_text = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2), MaxLengthValidator(100)],
    )
    url = models.ImageField(upload_to=None)
    productline = models.ForeignKey(
        ProductLine,
        on_delete=models.CASCADE,
        related_name="product_image",
    )
    order = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["productline", "order"],
                name="unique_order_for_product",
            )
        ]

    def save(self, *args, **kwargs):
        if self.order is None:
            max_order = ProductImage.objects.filter(
                productline=self.productline
            ).aggregate(models.Max("order"))["order__max"]

            self.order = (max_order or 0) + 1

            super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)
