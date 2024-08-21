from rest_framework import serializers

from product.models import Brand, Category, Product


class CategorySerializer(serializers.ModelField):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelField):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()

    class Meta:
        model = Product
        fields = "__all__"
