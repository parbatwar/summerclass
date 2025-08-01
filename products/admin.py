from django.contrib import admin
from .models import Category, Product
from django.utils.html import format_html

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')

class ProductAdmin(admin.ModelAdmin):
  exclude = ('created_at',)
  list_display = ('id', 'name', 'category', 'price', 'stock', 'status', 'image_preview')
  search_fields = ("name",)
  list_filter = ("category",)
  readonly_fields = ('image_preview',)

  def image_preview(self, obj):
    if obj.product_image:
      return format_html('<img src="{}" width="80" height="80" style="object-fit: cover;" />', obj.product_image.url)
    return "No Image"
  image_preview.short_description = 'Image Preview'

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)  