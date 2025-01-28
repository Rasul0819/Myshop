from django.contrib import admin
from . import models
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields = ('category',)

admin.site.register(models.Category,CategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('brandname',)
    list_filter = ('brandname',)

admin.site.register(models.Brand,BrandAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product','brand','category','price','available')
    list_editable = ('available','price')
    list_filter = ('available','brand','product','category')
    search_fields = ('product','brand')
admin.site.register(models.Product,ProductAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('stars','product',)
    list_filter = ('stars','product',)
