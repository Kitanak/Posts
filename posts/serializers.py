from rest_framework import serializers

from posts.models import (
    Category,
    Subcategory,
    Product,
)


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = (
            "id",
            "title",
        )


class SubcategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subcategory
        fields = (
            "id",
            "title",
        )


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "descriptions",
            "image",
            "price",
        )
