from rest_framework import serializers

from .models import QueryHistory


class QueryHistorySerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = QueryHistory
        fields = '__all__'
