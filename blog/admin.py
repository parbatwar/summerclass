from django.contrib import admin
from.models import Category, Blog

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')

class BlogAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'content', 'category')

# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog,BlogAdmin)