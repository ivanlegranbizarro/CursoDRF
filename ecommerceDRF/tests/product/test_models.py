import pytest

pytestmark = pytest.mark.django_db


class TestCategporyModel:
    def test_str_method(self, category_factory):
        category = category_factory()
        assert category.__str__() == category.name


class TestBrandModel:
    def test_str_method(self, brand_factory):
        brand = brand_factory()
        assert brand.__str__() == brand.name


class TestProductModel:
    def test_str_method(self, product_factory):
        product = product_factory()
        assert product.__str__() == product.slug


class TestProductLineModel:
    def test_order_equals_1_by_default(self, product_line_factory):
        product_line = product_line_factory()
        assert product_line.order == 1

    def test_str_method(self, product_line_factory):
        product_line = product_line_factory()
        assert product_line.__str__() == str(product_line.product)
