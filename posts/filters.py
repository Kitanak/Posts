from django_filters import rest_framework as filters
from django_filters import FilterSet

from posts.models import Category


class ProductFilterSet(FilterSet):
    price_from = filters.NumberFilter(field_name='price',lookup_expr='lt')
    price_to = filters.NumberFilter(field_name='price',lookup_expr='gt')
    categorys = filters.ModelMultipleChoiceFilter(
        field_name='category__id',
        to_field_name='id',
        queryset=Category.objects.all(),
    )
