from rest_framework import serializers

from product.models import Brand, Category, Product, ProductLine


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    brand_name = serializers.SerializerMethodField()
    product_line_data = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "is_digital",
            "category_name",
            "brand_name",
            "product_line_data",
        ]

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None

    def get_brand_name(self, obj):
        return obj.brand.name if obj.brand else None

    def get_product_line_data(self, obj):
        return [
            {
                "price": line.price,
                "sku": line.sku,
                "stock_qty": line.stock_qty,
            }
            for line in obj.product_line.all()
        ]
