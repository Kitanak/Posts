from rest_framework.viewsets import ModelViewSet

from django_filters import rest_framework as filters

from posts.filters import ProductFilterSet
from posts.models import (
    Category,
    Subcategory,
    Product
)
from posts.serializers import (
    CategorySerializer,
    SubcategorySerializer,
    ProductSerializer,
    ImageSerializer,
)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryViewSet(ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class ImageViewSet(ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = ImageSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.order_by('created_at')
    serializer_class = ProductSerializer
    filterset_class = ProductFilterSet
    filter_backends = (filters.DjangoFilterBackend,)
