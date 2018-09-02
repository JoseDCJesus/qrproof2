from django.contrib import admin

# Register your models here.

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['product_name', 'company_name', 'origin', 'sale_place', 'sales', 'sub_date']}),
    ]

    list_display = ('product_name', 'company_name', 'origin', 'sale_place')

admin.site.register(Product, ProductAdmin)
