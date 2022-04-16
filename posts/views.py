from rest_framework.viewsets import ModelViewSet

from posts.models import (
    Category,
    Subcategory,
    Product
)
from posts.serializers import (
    CategorySerializer,
    SubcategorySerializer,
    ProductSerializer,
)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryViewSet(ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
