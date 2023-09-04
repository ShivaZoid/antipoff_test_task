from decimal import Decimal
import re

from django.core.exceptions import ValidationError


def validate_cadastre_number(value):
    pattern = r'^\d{2}:\d{2}:\d{7}:\d{3}$'
    if not re.match(pattern, value):
        raise ValidationError(
            'Неправельно введен кадастровый номер. Пример: "77:01:0001012:123"'
        )


def validate_latitude(value):
    latitude = Decimal(str(value))
    if latitude > Decimal('90.0000000') or latitude < Decimal('-90.0000000'):
        raise ValidationError(
            "Широта должна быть между -90.0000000 и +90.0000000"
        )


def validate_longitude(value):
    longitude = Decimal(str(value))
    if longitude > Decimal('180.0000000') or longitude < Decimal('-180.0000000'):
        raise ValidationError(
            "Долгота должна быть между -180.0000000 и +180.0000000"
        )
