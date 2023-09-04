from django.contrib import admin

from .models import QueryHistory, FakeServer


admin.site.register(FakeServer)


@admin.register(QueryHistory)
class QueryAdmin(admin.ModelAdmin):
    """Конфигурация отображения данных.

    Attributes:
        list_display: отображаемые поля.
        search_fields: интерфейс для поиска.
        list_filter: возможность фильтрации.
    """

    list_display = (
        'cadastre_number',
        'latitude',
        'longitude',
        'response',
        'timestamp',
    )
    search_fields = ('cadastre_number', 'response',)
    list_filter = ('cadastre_number', 'response',)
    empty_value_display = '-пусто-'
