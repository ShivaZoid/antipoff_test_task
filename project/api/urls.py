from django.urls import path

from .views import (QueryView,
                    QueryHistoryView,
                    QueryResultView,
                    PingView)


app_name = 'api'


urlpatterns = [
    path('query/', QueryView.as_view(), name='query'),
    path('history/', QueryHistoryView.as_view(), name='history'),
    path(
        'result/<str:cadastre_number>/',
        QueryResultView.as_view(),
        name='result'
    ),
    path('ping/', PingView.as_view(), name='ping'),
]
