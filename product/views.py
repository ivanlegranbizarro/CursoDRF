from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing categories
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing brands
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing products
    """

    queryset = (
        Product.objects.all()
        .select_related("category", "brand")
        .prefetch_related("product_line")
    )
    lookup_field = "slug"

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        """
        This is an endpoint for listing all products
        """
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @extend_schema(responses=ProductSerializer)
    @action(
        methods=["get"],
        detail=False,
        url_path=r"category/(?P<category>[\w\s-]+)/all",
        url_name="list_products_by_category",
    )
    def list_product_by_category(self, request, category=None):
        """
        This is and enpoint for listing products by category
        """
        serializer = ProductSerializer(
            self.queryset.filter(category__name=category), many=True
        )
        return Response(serializer.data)

    @extend_schema(responses=ProductSerializer)
    def retrieve(self, request, slug=None):
        """
        This is an endpoint for retrieving a single product
        """
        product = get_object_or_404(self.queryset, slug=slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
