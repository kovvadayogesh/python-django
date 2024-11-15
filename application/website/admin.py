from django.contrib import admin
from . models import Category,Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','product_sku','product_price','product_qty')
    search_fields = ('product_name',)



admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
