from django.db import IntegrityError
from django.http import HttpResponseServerError
from rest_framework.views import exception_handler as drf_exception_handler


def custom_exception_handler(exc, context):
    response = drf_exception_handler(exc, context)

    if isinstance(exc, IntegrityError):
        response = HttpResponseServerError("Такой кадастровый номер уже существует, можете посмотреть его <a href='/api/history/'>тут</a>")

    return response
