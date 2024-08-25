import json
import pytest

pytestmark = pytest.mark.django_db


class TestProductViewSet:
    @pytest.fixture(autouse=True)
    def setup(self, product_factory):
        self.product = product_factory()

    def test_get_product_by_category(self, api_client):
        url = f"/api/product/category/{self.product.category.name}/all/"

        response = api_client.get(url)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_get_product_by_slug(self, api_client):
        url = f"/api/product/{self.product.slug}/"

        response = api_client.get(url)
        assert response.status_code == 200
        assert json.loads(response.content)["slug"] == self.product.slug
