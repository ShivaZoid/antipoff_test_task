from rest_framework import serializers

from .models import Query


class QuerySerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S",
        read_only=True,
        required=False
    )
    response = serializers.BooleanField(default=True)

    class Meta:
        model = Query
        fields = '__all__'
