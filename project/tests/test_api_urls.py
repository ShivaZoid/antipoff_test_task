from django.urls import reverse, resolve

from api.views import (
    QueryView,
    QueryHistoryView,
    QueryResultView,
    PingView
)


def test_query_url():
    url = reverse('api:query')
    view = resolve(url).func.view_class
    assert view == QueryView


def test_query_history_url():
    url = reverse('api:history')
    view = resolve(url).func.view_class
    assert view == QueryHistoryView


def test_query_result_url():
    url = reverse('api:result', kwargs={'cadastre_number': '77:01:0001012:123'})
    view = resolve(url).func.view_class
    assert view == QueryResultView


def test_ping_url():
    url = reverse('api:ping')
    view = resolve(url).func.view_class
    assert view == PingView
