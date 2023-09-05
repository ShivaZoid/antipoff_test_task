from decimal import Decimal

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Query, FakeServer


@pytest.mark.django_db
def test_query_view_valid_data():
    client = APIClient()
    data = {
        'cadastre_number': '77:01:0001012:123',
        'latitude': 55.1234567,
        'longitude': 37.9876543
    }
    response = client.post(reverse('api:query'), data, format='json')
    assert response.status_code == status.HTTP_202_ACCEPTED


@pytest.mark.django_db
def test_query_view_invalid_data():
    client = APIClient()
    data = {
        'cadastre_number': '0:0:0:0',
        'latitude': -100.0,
        'longitude': -200.0
    }
    response = client.post(reverse('api:query'), data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_query_history_view():
    client = APIClient()
    response = client.get(reverse('api:history'))
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_query_result_view():
    client = APIClient()
    query = Query.objects.create(
        cadastre_number='77:01:0001012:123',
        latitude=55.1234567,
        longitude=37.9876543,
        response=True
    )
    response = client.get(
        reverse('api:result', kwargs={'cadastre_number': '77:01:0001012:123'})
    )
    assert response.status_code == status.HTTP_200_OK

    response_data = response.data
    assert 'result' in response_data
    assert response_data['result'] is True


@pytest.mark.django_db
def test_query_result_view_not_found():
    client = APIClient()
    response = client.get(
        reverse('api:result', kwargs={'cadastre_number': 'nonexistent_number'})
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
