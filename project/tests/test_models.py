from decimal import Decimal

import pytest
from django.core.exceptions import ValidationError
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Query, FakeServer


@pytest.mark.django_db
def test_create_query():
    query = Query.objects.create(
        cadastre_number='77:01:0001012:123',
        latitude=55.1234567,
        longitude=37.9876543,
        response=True
    )
    assert query.pk is not None


@pytest.mark.django_db
def test_query_view_invalid_data():
    client = APIClient()
    data = {
        'cadastre_number': '4:0001:101:77:',
        'latitude': -100.0,
        'longitude': 200.0,
    }
    response = client.post(reverse('api:query'), data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Проверка наличия сообщений об ошибках в ответе
    assert 'cadastre_number' in response.data
    assert 'latitude' in response.data
    assert 'longitude' in response.data

    # Проверка текста сообщений об ошибках
    assert response.data['cadastre_number'] == [
        "Неправельно введен кадастровый номер. Пример: \"77:01:0001012:123\""
    ]
    assert response.data['latitude'] == [
        "Широта должна быть между -90.0000000 и +90.0000000"
    ]
    assert response.data['longitude'] == [
        "Долгота должна быть между -180.0000000 и +180.0000000"
    ]


@pytest.mark.django_db
def test_create_fake_server():
    fake_server = FakeServer.objects.create(run=True)
    assert fake_server.pk is not None
