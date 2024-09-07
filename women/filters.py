from django_filters.rest_framework import FilterSet
from women.models import Women


class WomenFilter(FilterSet):
    class Meta:
        model = Women
        fields = {"time_create": ["exact"], "id": ["gt", "lt"]}
