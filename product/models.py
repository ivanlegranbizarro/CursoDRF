from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Category(MPTTModel):
    name = models.CharField(
        "Name",
        max_length=50,
        validators=[MinLengthValidator(2), MaxLengthValidator(50)],
        null=False,
        blank=False,
    )
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(
        "Name",
        max_length=50,
        validators=[MinLengthValidator(2), MaxLengthValidator(50)],
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        "Name",
        max_length=50,
        validators=[MinLengthValidator(2), MaxLengthValidator(50)],
        null=False,
        blank=False,
    )
    description = models.TextField(
        "Description",
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

    def __str__(self):
        return self.name
