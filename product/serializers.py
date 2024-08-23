from rest_framework import serializers

from product.models import Brand, Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()

    class Meta:
        model = Product
        fields = "__all__"
