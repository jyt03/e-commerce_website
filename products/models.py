from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

    @staticmethod
    def get_products_by_name(names):
        return Product.objects.filter(name=names)
