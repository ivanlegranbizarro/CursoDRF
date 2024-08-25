import factory

from product.models import Brand, Category, Product, ProductLine


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f"Category {n}")


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Sequence(lambda n: f"Brand {n}")


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: f"Product {n}")
    description = factory.Sequence(lambda n: f"Description {n}")
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
    is_digital = factory.Faker("boolean")


class ProductLineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductLine

    product = factory.SubFactory(ProductFactory)
    price = factory.Faker(
        "pyfloat",
        left_digits=4,
        right_digits=2,
        max_value=1000,
    )
    sku = factory.Faker("ean", length=8)
    stock_qty = factory.Faker("pyint", min_value=0, max_value=100)
    order = None
