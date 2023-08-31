from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import QueryHistory
from .serializers import QueryHistorySerializer


class QueryView(APIView):
    def post(self, request):
        cadastre_number = request.data.get('cadastre_number')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        # эмулируем обработку запроса внешним сервером.
        import time
        time.sleep(60)

        # ответ от внешнего сервера.
        response = True

        query_history = QueryHistory.objects.create(
            cadastre_number=cadastre_number,
            latitude=latitude,
            longitude=longitude,
            response=response
        )
        query_history.save()

        return Response(
            {'message': 'Query processed and saved'},
            status=status.HTTP_202_ACCEPTED
        )


class QueryHistoryView(APIView):
    """Получить историю запросов из базы данных и вернуть в виде списка."""
    def get(self, request):
        query_history = QueryHistory.objects.all()
        serializer = QueryHistorySerializer(query_history, many=True)
        return Response(serializer.data)
