from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=10)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=10)
    product_sku = models.IntegerField()
    product_price = models.DecimalField(decimal_places=3,max_digits=5)
    product_qty = models.IntegerField()

    def __str__(self):
        return self.product_name


