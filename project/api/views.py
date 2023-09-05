from decimal import Decimal
import time

from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Query, FakeServer
from .serializers import QuerySerializer


class QueryView(APIView):
    def post(self, request):
        serializer = QuerySerializer(data=request.data)
        if serializer.is_valid():
            cadastre_number = serializer.validated_data['cadastre_number']
            latitude = serializer.validated_data['latitude']
            longitude = serializer.validated_data['longitude']

            # эмулируем обработку запроса внешним сервером.
            time.sleep(5)
            response = True

            query_history = Query.objects.create(
                cadastre_number=cadastre_number,
                latitude=latitude,
                longitude=longitude,
                response=response
            )

            return Response(
                {'message': 'Query processed and saved'},
                status=status.HTTP_202_ACCEPTED
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class QueryHistoryView(APIView):
    """Получить историю запросов из базы данных и вернуть в виде списка."""
    def get(self, request):
        query_history = Query.objects.all()
        serializer = QuerySerializer(query_history, many=True)
        return Response(serializer.data)


class QueryResultView(APIView):
    def get(self, request, cadastre_number):
        try:
            query_history = Query.objects.get(
                cadastre_number=cadastre_number
            )
            response = query_history.response
            return Response({'result': response}, status=status.HTTP_200_OK)
        except Query.DoesNotExist:
            return Response(
                {'error': 'Query not found'},
                status=status.HTTP_404_NOT_FOUND
            )


class PingView(APIView):
    def get(self, request):
        try:
            fake_server = FakeServer.objects.latest('id')
            if fake_server.run:
                return Response(
                    {'message': 'Server is running'},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {'message': 'Server is not working'},
                    status=status.HTTP_503_SERVICE_UNAVAILABLE
                )
        except FakeServer.DoesNotExist:
            return Response(
                {'error': 'Server settings not found'},
                status=status.HTTP_404_NOT_FOUND
            )
