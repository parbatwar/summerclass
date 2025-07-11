from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')

class ProductAdmin(admin.ModelAdmin):
  exclude = ('create_at',)
  list_display = ('id', 'name', 'category', 'price', 'stock', 'status')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)  