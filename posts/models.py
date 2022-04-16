from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)


class Subcategory(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='subcategorys')


class Product(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.TextField(null=True,blank=True)
    price = models.DecimalField(decimal_places=3,max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE,related_name='products')

class Image(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')
