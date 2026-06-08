from django.contrib import admin
from .models import Category, Menu

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_highlight')
    list_filter = ('category', 'is_highlight')
    search_fields = ('name', 'description')
