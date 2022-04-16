from rest_framework import serializers

from posts.models import (
    Category,
    Subcategory,
    Product,
    Image,
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
            'category',
        )


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "descriptions",
            "images",
            "price",

            'subcategory',
        )
        read_only_fields = (
            'images',
        )


class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Image
        fields = (
            "id",
            "image",
            "product",
        )

