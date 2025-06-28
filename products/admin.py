from django.contrib import admin
from .models import Product, Category, WaxType, CandleSize, Scent


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

    filter_horizontal = (
        'available_scents',
        'available_wax_types',
        'available_sizes',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ScentAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name')
    ordering = ('name',)


class WaxTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name', 'price_modifier')
    ordering = ('name',)


class CandleSizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name', 'price_modifier')
    ordering = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(WaxType, WaxTypeAdmin)
admin.site.register(Scent, ScentAdmin)
admin.site.register(CandleSize, CandleSizeAdmin)
