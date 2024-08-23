import json

import pytest

pytestmark = pytest.mark.django_db


class TestCastegoryEndpoints:
    endpoint = "/api/category/"

    @pytest.mark.django_db
    def test_category_get(self, category_factory, api_client):
        category_factory.create_batch(10)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 10


class TestBrandEndpoints:
    endpoint = "/api/brand/"

    def test_brand_get(self, brand_factory, api_client):
        brand_factory.create_batch(10)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 10


class TestProductEndpoints:
    endpoint = "/api/product/"

    def test_product_get(self, product_factory, api_client):
        product_factory.create_batch(10)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 10
