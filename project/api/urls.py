from django.urls import path

from .views import QueryView, QueryHistoryView


app_name = 'api'


urlpatterns = [
    path('query/', QueryView.as_view(), name='query'),
    path('history/', QueryHistoryView.as_view(), name='history'),
]
