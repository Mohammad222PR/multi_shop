from django.contrib import admin
from .models import Product, Information, Size, Color

class InformationInline(admin.StackedInline):
    model = Information
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'product')
    inlines = [InformationInline]

admin.site.register(Size)
admin.site.register(Color)
