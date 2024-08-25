import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from .factories import (
    BrandFactory,
    CategoryFactory,
    ProductFactory,
    ProductLineFactory,
)

register(CategoryFactory)
register(ProductFactory)
register(BrandFactory)
register(ProductLineFactory)


@pytest.fixture
def api_client():
    return APIClient()
