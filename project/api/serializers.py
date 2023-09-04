from rest_framework import serializers

from .models import QueryHistory


class QueryHistorySerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S",
        read_only=True,
        required=False
    )
    response = serializers.BooleanField(default=True)

    class Meta:
        model = QueryHistory
        fields = '__all__'
