from django.contrib import admin
from .models import Category, Product, Brand

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'brand',
        'price',
        'category',
    )
    ordering = ('name',)
    list_filter = ('category', 'brand',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
    ordering = ('friendly_name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
