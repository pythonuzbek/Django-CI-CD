import pytest
from django.test import Client
from rest_framework import status
from rest_framework.reverse import reverse_lazy


@pytest.fixture
def api_client():
    return Client()

@pytest.mark.django_db
class TestCategory:
    def test_get_all_category(self,api_client):
        url = reverse_lazy('category-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_create_category(self,api_client):
        url = reverse_lazy('category-list')
        data = {
            'name': 'Toshkent'
        }
        response = api_client.post(url,data)
        assert response.status_code == status.HTTP_201_CREATED
