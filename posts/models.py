from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)


class Subcategory(models.Model):
    title = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(decimal_places=3,max_digits=10)
    
    created_at = models.DateTimeField(auto_now_add=True)
