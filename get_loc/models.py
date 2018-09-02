from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200 )
    origin = models.CharField(max_length=200)
    sale_place = models.CharField(max_length=200)
    sales = models.IntegerField(default=0)
    sub_date = models.DateTimeField('date submited')


    def __str__(self):
        return self.product_name



